from fastapi import FastAPI, HTTPException,Request
from app.models  import UserCreate,Task
from app.db import *
from mongoengine import connect,ValidationError


app = FastAPI()


@app.post("/register",) 
async def register_user(request:Request):
    data_status={"response":"","status":0}
    body=await request.json()
    userName=body.get("username")
    email=body.get("email")
    password=body.get("password")
    type=body.get("type")
    try:
        userQuerySet=UserCreate.objects(userEmail=email).first() # db query
        if userQuerySet:
            data_status={
                "response":"User Already Exist",
                "status":1,
            }
        else:
            registerusers= UserCreate (
            userName=userName,
            userEmail=email,
            password=password,
            type=type

        )
            registerusers.save()
            data_status={
            "response":str(type)+" Register Succesfully",
            "status":1,
            }
        
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    return data_status

@app.post('/login',)
async def login(request:Request):
    data_status={"response":"","status":0}
    body= await request.json()
    email=body.get("email")
    password=body.get('password')
    try:
        user = UserCreate.objects(userEmail=email,password=password).first()
        if not user:
            data_status={
                "response":"User Not Found Please Register"
            }
        else:
         data_status={
            "response":{
                "userId":str(user.id),
                "userName":user.userName,
                "userEmail":user.userEmail,
                "type":user.type,
            }
         }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return data_status



@app.post("/tasks/add",)
async def add_task(request: Request):
    data_status={"response":"","status":0}
    body = await request.json()
    userId = body.get("userId")
    title = body.get("tasktitle")
    taskdescription = body.get("taskDescription")
    taskName=body.get("taskName")

    try:
        user = UserCreate.objects(id=userId).first()
        if not user:
            data_status={
                "response":"User Not Found Please Register",
                "status":1,
            }

        task = Task(
            tasktitle=title,
            taskName=taskName,
            taskDescription=taskdescription,  
        )
        task.save()
        data_status={
            "response":{
                "message":"task added successfully",
                "taskId":str(task.id)
            },
            "status":1
        }

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return data_status



    
@app.put("/task/update")
async def update_task(request:Request):
    data_status={"response":"","status":0}
    body = await request.json()
    userId = body.get("userId")
    title = body.get("title")
    taskId=body.get("taskId")
    taskName=body.get("taskName")
    description = body.get("description")

    try:
        user = UserCreate.objects(id=userId).first()
        if not user:
            data_status={
                "response":"User Not Found",
                "status":1,
            }
        
        task_query = Task.objects(id=taskId).first()
        if not task_query:
            data_status = {
                "response": "Task not found",
                "status": 1,
            }
        else:
            task_query.taskName = taskName
            task_query.tasktitle = title
            task_query.taskDescription = description
            task_query.save()

            data_status = {
                "response": "Task updated successfully",
                "status": 1
            }

    except ValidationError as e:
        raise HTTPException(status_code=400,detail=str(e))
    return data_status



@app.delete("/task/delete")
async def delete_task(request:Request):
    data_status={"raspone":"","status":0}
    body = await request.json()
    userId = body.get("userId")
    taskId = body.get("taskId")  

    try:
        user = UserCreate.objects(id=userId).first()
        if not user:
            data_status={
                "response":"User Not Found",
                "status":1,
            }


        task = Task.objects(id=taskId).first()
        if not task:
            data_status={
                "response":"Task not found",
                "status":1,
            }
        else:
            delete_task=task.delete()
            # delete_task.save() 
            data_status={
                "response": "Task deleted successfully",
                "status": 1
            }
    except ValidationError as e:
        raise HTTPException(status_code=400,detail=str(e))
    return data_status        
        



        






         


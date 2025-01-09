# @app.get("/users/{user_id}", response_model=dict)
# async def get_user(user_id: str):
#     user = User.objects(id=user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     return serialize_user(user)


# @app.put("/users/{user_id}", response_model=dict)
# async def update_user(user_id: str, user_update: UserUpdate):
#     user = User.objects(id=user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     update_data = {k: v for k, v in user_update.dict().items() if v is not None}
#     user.update(**update_data)
    
#     return {"message": "User updated successfully"}

# @app.delete("/users/{user_id}", response_model=dict)
# async def delete_user(user_id: str):
#     user = User.objects(id=user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     user.delete()
#     return {"message": "User deleted successfully"}
# @app.get("/users", response_model=list)
# async def list_users():
#     users = User.objects()
#     return [serialize_user(user) for user in users]



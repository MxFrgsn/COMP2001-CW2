# user.py
from flask import abort, make_response
from config import db
from models import users_schema, user_schema, User

def create(user): # done swagger, need test
    user_id = user.get('user_id')
    existing_user = user.query.filter(user.user_id == user_id).one_or_none()
    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"user with user_id {user_id} already exists")

def read_one(user_id): #done swagger, need test
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"User with user_id {user_id} not found")

def read_all():
    users = db.session.query(User).all() 
    return users.schema.dump(users)

def updateUserName(username,user_id): #done swagger, need test, need to do for all attributes
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()
    if existing_user:
        existing_user.username = username 
        db.session.commit()
        return {"message": f"User with ID {user_id} updated successfully."}, 200
    else:
        abort(404, f"User with user_id {user_id} not found")
    
def delete(user_id): #done swagger, need test
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"user with last name {user_id} has been deleted", 200)
    else:
        abort(404, f"user with last name {user_id} not found")

# should add a function to view what trails a user owns
# should add functions to update other user details like passwords, emails etc
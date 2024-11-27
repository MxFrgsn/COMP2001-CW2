# user.py
from flask import abort, make_response, request
from config import db
from models import users_schema, user_schema, User

def create(): # done swagger, need test
    user_data = request.get_json()  
    if not user_data:  
        abort(400, "No input data provided")
    user_id = user_data.get('user_id')
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()
    if existing_user is None:
        new_user = user_schema.load(user_data, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"User with user ID {user_id} already exists")

def read_one(user_id):
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"User with user ID {user_id} not found")

def read_all():
    users = db.session.query(User).all() 
    return users_schema.dump(users)

def update(user_id):
    # Patch is used instead of put, as put updates all fields, patch only updates the fields that are included in the request body
    user_data = request.get_json()  
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()
    
    if existing_user:
        # Update only the fields that were included in the request body
        if 'username' in user_data:
            existing_user.username = user_data['username']
        if 'email' in user_data:
            existing_user.email = user_data['email']
        if 'password' in user_data:
            existing_user.password = user_data['password']
        if 'role' in user_data:
            existing_user.role = user_data['role']
        db.session.commit()
        return make_response(f"User with ID {user_id} has been updated successfully.", 200)
    else:
        abort(404, f"User with ID {user_id} not found")
    
def delete(user_id): #done swagger, need test
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"User with user ID {user_id} has been deleted", 200)
    else:
        abort(404, f"User with user ID {user_id} not found")

# should add a function to view what users a user owns

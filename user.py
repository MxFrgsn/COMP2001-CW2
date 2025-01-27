# user.py
from flask import abort, make_response, request, session
from config import db
from models import users_schema, user_schema, User, Trail, limited_user_schema, limited_users_schema
import requests

def create():
    user_data = request.get_json()  
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
    if user is not None and session.get('role') == 'admin':
        return user_schema.dump(user)
    elif user is not None and session.get('role') != 'admin':
        return limited_user_schema.dump(user)
    else:
        abort(404, f"User with user ID {user_id} not found")

def read_all(name=None):
    query = User.query
    if name:
        query = query.filter(User.trail_name.ilike(f"%{name}%"))
    users = query.all()
    if session.get('role') != 'admin':
        return limited_users_schema.dump(users)
    else:
         return users_schema.dump(users)

def update(user_id):
    # Patch is used instead of put, as put updates all fields, patch only updates the fields that are included in the request body
    if session.get('user_id') != user_id and session.get('role') != 'admin':
        return make_response(f"User {user_id} cannot be updated, currently authenicated user {session.get('user_id')} is not an admin.", 400)
    
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
    
def delete(user_id): 
    if user_id == 1:
        return make_response(f"User with ID {user_id} cannot be deleted. This is the default admin user.", 403)
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()
    trails = Trail.query.filter(Trail.owner_id == user_id).all()

    if not session.get('user_id'):
        return make_response("No user is currently logged in.", 400)
    if session['user_id'] != user_id and session['role'] != 'admin':
        return make_response(f"User with ID {user_id} cannot be deleted. Only the user themselves or an admin can delete.", 403)

    if existing_user:
        # Mantains the trails that the user owns
        if trails:
            for trail in trails:
                trail.owner_id = 1
                db.session.add(trail)
        db.session.commit()
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"User with user ID {user_id} has been deleted", 200)
    else:
        abort(404, f"User with user ID {user_id} not found")

def authentication():
    auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'
    user_data = request.get_json()  

    credentials = {'email': user_data['email'], 'password': user_data['password']}
    try:
        response = requests.post(auth_url, json=credentials)
        response.raise_for_status() 
        
        if response.json() == ["Verified", "True"]:  
            logged_in_user = User.query.filter(User.email == user_data['email']).one_or_none()
            if not logged_in_user:
                return make_response("User not found in the local database.", 404)
            session['user_id'] = logged_in_user.user_id
            session['role'] = logged_in_user.role
            return make_response(f"Authenticated successfully. User ID: {logged_in_user.user_id}", 200)
        else:
            return make_response("Authentication failed. Invalid credentials.", 401)
    except requests.exceptions.RequestException as e:
        return make_response(f"Error communicating with authentication service: {str(e)}", 500)
    except Exception as e:
        return make_response(f"An unexpected error occurred: {str(e)}", 500)


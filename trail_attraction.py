# trail_attraction.py
from flask import abort, make_response, request
from config import db
from models import trail_attraction_schema, trail_attractions_schema, TrailAttraction   

def create():
    trail_attraction_data = request.get_json()  
    if not trail_attraction_data:  
        abort(400, "No input data provided")
    trail_id = trail_attraction_data.get('trail_id') # change this
    existing_trail_attraction = TrailAttraction.query.filter(TrailAttraction.user_id == user_id).one_or_none()
    if existing_trail_attraction is None:
        new_user = trail_attraction_schema.load(trail_attraction_data, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return trail_attraction_schema.dump(new_user), 201
    else:
        abort(406, f"Trail Attraction with user ID {user_id} already exists")

# read all trail attractions for a specific trail
# create a new attraction to a specific trail
# delete a specific attraction from a specific trail

def read_one(user_id):
    user = TrailAttraction.query.filter(TrailAttraction.user_id == user_id).one_or_none()
    if user is not None:
        return trail_attraction_schema.dump(user)
    else:
        abort(404, f"Trail Attraction with user ID {user_id} not found")

def read_all():
    users = db.session.query(TrailAttraction).all() 
    return trail_attractions_schema.dump(users)
    
def delete(user_id): 
    existing_trail_attraction = TrailAttraction.query.filter(TrailAttraction.user_id == user_id).one_or_none()
    if existing_trail_attraction:
        db.session.delete(existing_trail_attraction)
        db.session.commit()
        return make_response(f"Trail Attraction with user ID {user_id} has been deleted", 200)
    else:
        abort(404, f"Trail Attraction with user ID {user_id} not found")

# trail_attraction.py
from flask import abort, make_response, request
from config import db
from models import trail_attraction_schema, trail_attractions_schema, TrailAttraction

def create():
    trail_attraction_data = request.get_json()  
    if not trail_attraction_data:  
        abort(400, "No input data provided")
    trail_id = trail_attraction_data.get('trail_id') 
    attraction_id = trail_attraction_data.get('attraction_id')
    existing_trail_attraction = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id,TrailAttraction.attraction_id== attraction_id).one_or_none()
    if existing_trail_attraction is None:
        new_user = trail_attraction_schema.load(trail_attraction_data, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return trail_attraction_schema.dump(new_user), 201
    else:
        abort(406, f"Trail Attraction with ID {attraction_id} already tied to Trail with ID {trail_id}")

def read_all_tied_to_trail_id(trail_id): # need test
    trail_attraction = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id).all()
    if trail_attraction is not None:
        return trail_attractions_schema.dump(trail_attraction)
    else:
        abort(404, f"Trail Attractions with Trail ID {trail_id} not found")

def read_all_attraction_tied_to_trails(attraction_id): # need test
    trail_attraction = TrailAttraction.query.filter(TrailAttraction.attraction_id == attraction_id).all()
    if trail_attraction is not None:
        return trail_attractions_schema.dump(trail_attraction)
    else:
        abort(404, f"No Trails found with Attraction ID {attraction_id}")

def read_all(): # need test
    trail_attractions = db.session.query(TrailAttraction).all() 
    return trail_attractions_schema.dump(trail_attractions)
    
def delete_all_attractions_tied_to_trail(trail_id):  # need test
    existing_trail_attractions = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id).all() 
    if existing_trail_attractions:
        for attraction in existing_trail_attractions:
            db.session.delete(attraction)
        db.session.commit()
        return make_response(f"All Attractions IDs tied to the trail ID {trail_id} has been deleted", 200)
    else:
        abort(404, f"trail with ID {trail_id} not found")

def delete_one_attraction_tied_to_trail(trail_id, attraction_id): # need test
    existing_trail_attraction = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id, TrailAttraction.attraction_id == attraction_id).one_or_none()
    if existing_trail_attraction:
        db.session.delete(existing_trail_attraction)
        db.session.commit()
        return make_response(f"Attraction ID {attraction_id} tied to the trail ID {trail_id} has been deleted", 200)
    else:
        abort(404, f"Attraction ID {attraction_id} tied to the trail ID {trail_id} not found")
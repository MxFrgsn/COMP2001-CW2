# trail_attraction.py
from flask import abort, make_response, request, session
from config import db
from models import trail_attraction_schema, trail_attractions_schema, TrailAttraction, Trail

def create():  
    trail_attraction_data = request.get_json()  
    trail_id = trail_attraction_data.get('trail_id') 
    attraction_id = trail_attraction_data.get('attraction_id')
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    
    if session.get('role') != 'admin' and session.get('user_id') != existing_trail.owner_id: 
        return make_response(f"Trail Attraction cannot be created, currently authenicated user {session.get('user_id')} is not an admin or the owner of the trail.", 400)
    
    existing_trail_attraction = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id,TrailAttraction.attraction_id== attraction_id).one_or_none()
    if existing_trail_attraction is None:
        new_user = trail_attraction_schema.load(trail_attraction_data, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return trail_attraction_schema.dump(new_user), 201
    else:
        abort(406, f"Trail Attraction with ID {attraction_id} already tied to Trail with ID {trail_id}")

def read_attractions_or_trails(id, type): 
    if type == 'trail':
        attribute = 'trail_id'
    elif type == 'attraction':
        attribute = 'attraction_id'

    trail_attraction = TrailAttraction.query.filter(getattr(TrailAttraction, attribute) == id).all()
    if trail_attraction:
        return trail_attractions_schema.dump(trail_attraction)
    else:
        abort(404, "No Trail Attraction found for the given ID")
    
def read_all(): 
    trail_attractions = TrailAttraction.query.all()
    return trail_attractions_schema.dump(trail_attractions)

def delete_all_tied_to_trail(trail_id): 
    existing_trail_attractions = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id).all()
    owner_id = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if owner_id:
        owner_id = owner_id.owner_id
    else:
        abort(404, f"Trail ID {trail_id} not found")

    if session.get('role') != 'admin' and session.get('user_id') != owner_id:
        return make_response(f"Trail Attraction cannot be deleted, currently authenicated user {session.get('user_id')} is not an admin or the owner of the trail {trail_id}.", 400)
    if existing_trail_attractions:
        for attraction in existing_trail_attractions:
            db.session.delete(attraction)
        db.session.commit()
        return make_response(f"All Attractions tied to trail ID {trail_id} have been deleted", 204)
    else:
        abort(404, f"No attractions found linked to trail ID {trail_id}")

def delete(trail_id,attraction_id): 
    if session.get('role') != 'admin':
        return make_response(f"Trail Attraction cannot be deleted, currently authenicated user {session.get('user_id')} is not an admin.", 400)
    existing_trail_attraction = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id,TrailAttraction.attraction_id == attraction_id).one_or_none()
    if existing_trail_attraction:
        db.session.delete(existing_trail_attraction)
        db.session.commit()
        return make_response(f"Attraction ID {attraction_id} tied to the trail ID {trail_id} has been deleted", 204)
    else:
        abort(404, f"Attraction ID {attraction_id} tied to the trail ID {trail_id} not found")
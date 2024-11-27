# trail.py
from flask import abort, make_response, request
from config import db
from models import trail_schema, trails_schema, Trail, TrailAttraction 

def create(): 
    trail_data = request.get_json()  
    trail_id = trail_data.get('trail_id')
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail is None:
        new_trail = trail_schema.load(trail_data, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f"trail with trail_id {trail_id} already exists")

def read_one(trail_id):
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with trail_id {trail_id} not found")

def read_all(): 
    trails = db.session.query(Trail).all()
    return trails_schema.dump(trails)

def update(trail_id):
    trail_data = request.get_json()  
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    
    if existing_trail:
        # Update only the fields that were included in the request body
        if 'trail_name' in trail_data:
            existing_trail.trail_name = trail_data['trail_name']
        if 'difficulty' in trail_data:
            existing_trail.difficulty = trail_data['difficulty']
        if 'length' in trail_data:
            existing_trail.length = trail_data['length']
        if 'traffic' in trail_data:
            existing_trail.traffic = trail_data['traffic']
        if 'duration' in trail_data:
            existing_trail.duration = trail_data['duration']
        if 'elevation_gain' in trail_data:
            existing_trail.elevation_gain = trail_data['elevation_gain']
        if 'route_type' in trail_data:
            existing_trail.route_type = trail_data['route_type']
        if 'summary' in trail_data:
            existing_trail.summary = trail_data['summary']
        if 'description' in trail_data:
            existing_trail.description = trail_data['description']
        if 'location' in trail_data:
            existing_trail.location = trail_data['location']
        
        db.session.commit()
        return make_response(f"trail with ID {trail_id} has been updated successfully.", 200)
    else:
        abort(404, f"trail with ID {trail_id} not found")

def delete(trail_id): 
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    # Deleting all attractions associated with the trail, as trail id is a foreign key in the trail attraction table
    existing_trail_attractions = TrailAttraction.query.filter(TrailAttraction.trail_id == trail_id).all() 

    if existing_trail:
        for attraction in existing_trail_attractions:
            db.session.delete(attraction)
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"trail with ID {trail_id} has been deleted", 200)
    else:
        abort(404, f"trail with ID {trail_id} not found")

# should add update for every attribute of trail
# should i be able to view functions based on the name or user id of the trail owner?
# should i be able to view the attractions of a trail? in the read_one/read_all function?
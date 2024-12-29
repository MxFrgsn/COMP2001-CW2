# trail.py
from flask import abort, make_response, request, session
from config import db
from models import trail_schema, trails_schema, Trail, limited_trails_schema, limited_trail_schema

def create(): 
    trail_data = request.get_json()  
    new_trail = trail_schema.load(trail_data, session=db.session)
    db.session.add(new_trail)
    db.session.commit()
    return trail_schema.dump(new_trail)

def read_one(trail_id):
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if trail is not None:
        if session.get('role') == 'admin':
            return trail_schema.dump(trail)
        return limited_trail_schema.dump(trail)
    else:
        abort(404, f"Trail with trail_id {trail_id} not found")

def read_all(name=None): 
    query = Trail.query
    if name:
        query = query.filter(Trail.trail_name.ilike(f"%{name}%"))
    trails = query.all()
    if session.get('role') == 'admin':
        return trails_schema.dump(trails)
    return limited_trails_schema.dump(trails)

def update(trail_id):
    trail_data = request.get_json()  
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    print(session.get('role'))
    if session.get('role') != 'admin' and session.get('user_id') != existing_trail.owner_id:
        return make_response(f"Trail {trail_id} cannot be updated, currently authenicated user {session.get('user_id')} is not the owner of the trail.", 400)
    
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
    if session.get('user_id') != existing_trail.owner_id and session.get('role') != 'admin':
        return make_response(f"Trail {trail_id} cannot be deleted, currently authenicated user {session.get('user_id')} is not the owner of the trail.", 400)
    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"trail with ID {trail_id} has been deleted", 200)
    else:
        abort(404, f"trail with ID {trail_id} not found")

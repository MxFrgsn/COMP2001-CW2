# trail.py
from flask import abort, make_response, request
from config import db
from models import trail_schema, trails_schema, Trail, TrailAttraction 

def create(): # done swagger, done test
    trail_data = request.get_json()  
    if not trail_data:  
        abort(400, "No input data provided")

    trail_id = trail_data.get('trail_id')
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if existing_trail is None:
        new_trail = trail_schema.load(trail_data, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f"trail with trail_id {trail_id} already exists")

def read_one(trail_id): #done swagger, done test
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with trail_id {trail_id} not found")

def read_all(): # done swagger, done test
    trails = db.session.query(Trail).all()
    return trails_schema.dump(trails)

def updateTrailName(trail_name,trail_id):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if existing_trail:
        existing_trail.trail_name = trail_name 
        db.session.commit()
        return {"message": f"Trail with ID {trail_id} updated successfully."}, 200
    else:
        abort(404, f"Trail with ID {trail_id} not found")
    
def delete(trail_id): # done swagger, done test
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
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
# should add a function to view what locations a trail has
# should i be able to view functions based on the name or user id of the trail owner?
# should i be able to view the attractions of a trail? in the read_one/read_all function?
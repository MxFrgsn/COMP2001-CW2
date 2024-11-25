from flask import abort, make_response
from config import db
from models import trail_schema, trails_schema, Trail, Location

def create(trail):
    trail_id = trail.get('trail_id')
    existing_trail = trail.query.filter(trail.trail_id == trail_id).one_or_none()
    if existing_trail is None:
        new_trail = trail_schema.load(trail, session=db.session)
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
    trails = db.session.query(Trail).join(Location).all() # can i include attractions too?
    return trails_schema.dump(trails)

def updateTrailName(trail_name,trail_id):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if existing_trail:
        existing_trail.trail_name = trail_name 
        db.session.commit()
        return {"message": f"Trail with ID {trail_id} updated successfully."}, 200
    else:
        abort(404, f"Trail with trail_id {trail_id} not found")
    
def delete(trail_id):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"trail with last name {trail_id} has been deleted", 200)
    else:
        abort(404, f"trail with last name {trail_id} not found")

# should add update for every attribute of trail
# should add a function to view what locations a trail has
# should i be able to view functions based on the name or user id of the trail owner?
# should i be able to view the attractions of a trail? in the read_one/read_all function?
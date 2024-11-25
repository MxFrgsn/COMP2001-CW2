from flask import abort, make_response
from config import db
from models import trail_schema, trails_schema, Trail

def create():
    return "Trail created"

def read_one(trail_id): 
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with trail_id {trail_id} not found")

def read_all():
    return trails_schema.dump(Trail.query.all())

def update():
    return "Trail updated"

def delete():
    return "Trail deleted"

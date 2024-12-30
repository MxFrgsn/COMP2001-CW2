# trail_locationpt.py
from flask import abort, make_response, request, session
from config import db
from models import trail_locationpt_schema, trail_locationpts_schema, TrailLocationPt, Trail

def create():
    trail_locationpt_data = request.get_json()  
    trail_id = trail_locationpt_data.get('trail_id') 
    location_point_id = trail_locationpt_data.get('location_point_id')
    existing_trail_locationpt = TrailLocationPt.query.filter(TrailLocationPt.trail_id == trail_id,TrailLocationPt.location_point_id== location_point_id).one_or_none()
    existing_trial = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trial.owner_id != session.get('user_id') and session.get('role') != 'admin':
        return make_response(f"Trail Location Point cannot be created, currently authenicated user {session.get('user_id')} is not the owner of the trail or an admin.", 400)
    
    if existing_trail_locationpt is None:
        new_trail_locationpt = trail_locationpt_schema.load(trail_locationpt_data, session=db.session)
        db.session.add(new_trail_locationpt)
        db.session.commit()
        return trail_locationpt_schema.dump(new_trail_locationpt), 201
    else:
        abort(406, f"Trail Location Point with trail id {trail_id}  and location point id  {location_point_id} already exists.")

def read_locationpts_or_trails(id, type): 
    if type == 'trail':
        attribute = 'trail_id'
    elif type == 'location_point':
        attribute = 'location_point_id'

    trail_locationpt = TrailLocationPt.query.filter(getattr(TrailLocationPt, attribute) == id).all()
    if trail_locationpt:
        return trail_locationpts_schema.dump(trail_locationpt)
    else:
        abort(404, "No Trail Attraction found for the given ID")
    
def delete_all_tied_to_trail(trail_id):
    existing_trail_locationpts = TrailLocationPt.query.filter(TrailLocationPt.trail_id == trail_id).all()
    owner_id = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if owner_id:
        owner_id = owner_id.owner_id
    else:
        abort(404, f"Trail ID {trail_id} not found")

    if session.get('role') != 'admin' and session.get('user_id') != owner_id:
        return make_response(f"Trail Location Point cannot be deleted, currently authenicated user {session.get('user_id')} is not an admin or the owner of the trail {trail_id}.", 400)
    
    if existing_trail_locationpts:
        for trail_locationpt in existing_trail_locationpts:
            db.session.delete(trail_locationpt)
        db.session.commit()
        return make_response(f"All Trail Location Points tied to trail ID {trail_id} have been deleted", 204)
    else:
        abort(404, f"No trail location points found linked to trail ID {trail_id}")


def read_all():
    trail_locationpts = TrailLocationPt.query.all()
    return trail_locationpts_schema.dump(trail_locationpts)

def update(trail_id, location_point_id):
    trail_locationpt_data = request.get_json()  
    existing_trail_locationpt = TrailLocationPt.query.filter(TrailLocationPt.trail_id == trail_id == trail_id, TrailLocationPt.location_point_id == location_point_id).one_or_none()
    owner_id = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if owner_id:
        owner_id = owner_id.owner_id
    else:
        abort(404, f"Trail ID {trail_id} not found")

    if session.get('role') != 'admin' and session.get('user_id') != owner_id:
        return make_response(f"Trail Location Point cannot be udpated, currently authenicated user {session.get('user_id')} is not an admin or the owner of the trail {trail_id}.", 400)
   
    if existing_trail_locationpt:
        existing_trail_locationpt.order_number = trail_locationpt_data['order_number']
        db.session.commit()
        return make_response(f"Trail Location point with trail id {trail_id} and location point id {location_point_id} has been updated successfully.", 200)
    else:
        abort(404, f"Trail Location point with trail id {trail_id} and location point id {location_point_id} not found")

def delete(trail_id, location_point_id):
    existing_trail_locationpt = TrailLocationPt.query.filter(TrailLocationPt.trail_id == trail_id == trail_id, TrailLocationPt.location_point_id == location_point_id).one_or_none()
    owner_id = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    if owner_id:
        owner_id = owner_id.owner_id
    else:
        abort(404, f"Trail ID {trail_id} not found")

    if session.get('role') != 'admin' and session.get('user_id') != owner_id:
        return make_response(f"Trail Location Point cannot be deleted, currently authenicated user {session.get('user_id')} is not an admin or the owner of the trail {trail_id}.", 400)
   
    if existing_trail_locationpt:
        db.session.delete(existing_trail_locationpt)
        db.session.commit()
        return make_response(f"Trail Location point with trail id {trail_id} and location point id {location_point_id} has been deleted", 200)
    else:
        abort(404, f"Trail Location point with trail id {trail_id} and location point id {location_point_id} not found")


# location_point.py
from flask import abort, make_response, request
from config import db
from models import location_point_schema, location_points_schema, LocationPoint

def create(): 
    location_point_data = request.get_json()  
    location_point_id = location_point_data.get('location_point_id')
    existing_location_point = LocationPoint.query.filter(LocationPoint.location_point_id == location_point_id).one_or_none()

    if existing_location_point is None:
        new_location_point = location_point_schema.load(location_point_data, session=db.session)
        db.session.add(new_location_point)
        db.session.commit()
        return location_point_schema.dump(new_location_point), 201
    else:
        abort(406, f"Location Point with location point ID {location_point_id} already exists")

def read_one(location_point_id): 
    location_point = LocationPoint.query.filter(LocationPoint.location_point_id == location_point_id).one_or_none()
    if location_point is not None:
        return location_point_schema.dump(location_point)
    else:
        abort(404, f"Location Point with location point ID {location_point_id} not found")

def read_all(name=None): 
    query = LocationPoint.query
    if name:
        query = query.filter(LocationPoint.location_point_name.ilike(f"%{name}%"))
    location_points = query.all()
    return location_points_schema.dump(location_points)

def update(location_point_id):
    location_point_data = request.get_json()  
    existing_location_point = LocationPoint.query.filter(LocationPoint.location_point_id == location_point_id).one_or_none()
    
    if existing_location_point:
        # Update only the fields that were included in the request body
        if 'description' in location_point_data:
            existing_location_point.description = location_point_data['description']
        if 'latitude' in location_point_data:
            existing_location_point.latitude = location_point_data['latitude']
        if 'longitude' in location_point_data:
            existing_location_point.longitude = location_point_data['longitude']
        db.session.commit()
        return make_response(f"Location Point with ID {location_point_id} has been updated successfully.", 200)
    else:
        abort(404, f"Location Point with ID {location_point_id} not found")

def delete(location_point_id):
    existing_location_point = LocationPoint.query.filter(LocationPoint.location_point_id == location_point_id).one_or_none()
    if existing_location_point:
        db.session.delete(existing_location_point)
        db.session.commit()
        return make_response(f"Location Point with location point ID {location_point_id} has been deleted", 200)
    else:
        abort(404, f"Location Point with location point ID {location_point_id} not found")

from flask import abort, make_response, request
from config import db
from models import Attraction, attraction_schema, attractions_schema, TrailAttraction

def create():
    attraction_data = request.get_json()  
    attraction_id = attraction_data.get('attraction_id')
    existing_attraction = Attraction.query.filter(Attraction.attraction_id == attraction_id).one_or_none()

    if existing_attraction is None:
        new_attraction = attraction_schema.load(attraction_data, session=db.session)
        db.session.add(new_attraction)
        db.session.commit()
        return attraction_schema.dump(new_attraction), 201
    else:
        abort(406, f"Attraction with attraction ID {attraction_id} already exists")
        
def delete(attraction_id): 
    existing_attraction = Attraction.query.filter(Attraction.attraction_id == attraction_id).one_or_none()
    existing_trail_attractions = TrailAttraction.query.filter(TrailAttraction.attraction_id == attraction_id).all()
    if existing_attraction:
        for attraction in existing_trail_attractions:
            db.session.delete(attraction)
        db.session.delete(existing_attraction)
        db.session.commit()
        return make_response(f"Attraction with attraction ID {attraction_id} has been deleted", 200)
    else:
        abort(404, f"Attraction with attraction ID {attraction_id} not found")

def read_all(name=None): 
    query = Attraction.query
    if name:
        query = query.filter(Attraction.attraction_name.ilike(f"%{name}%"))
    attractions = query.all()
    return attractions_schema.dump(attractions)

def read_one(attraction_id):
    attraction = Attraction.query.filter(Attraction.attraction_id == attraction_id).one_or_none()
    if attraction is not None:
        return attraction_schema.dump(attraction)
    else:
        abort(404, f"Attraction with attraction ID {attraction_id} not found")

def update(attraction_id):
    attraction_data = request.get_json()  
    existing_attraction = Attraction.query.filter(Attraction.attraction_id == attraction_id).one_or_none()
    if existing_attraction:
        if 'attraction_name' in attraction_data:
            existing_attraction.attraction_name = attraction_data['attraction_name']
        db.session.commit()
        return make_response(f"Attraction with ID {attraction_id} has been updated successfully.", 200)
    else:
        abort(404, f"Attraction with ID {attraction_id} not found")

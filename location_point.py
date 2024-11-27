# location_point.py
from flask import abort, make_response, request
from config import db
from models import location_point_schema, location_points_schema, LocationPoint
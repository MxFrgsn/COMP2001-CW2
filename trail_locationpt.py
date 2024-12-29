# trail_locationpt.py
from flask import abort, make_response, request
from config import db
from models import trail_locationpt_schema, trail_locationpts_schema, TrailLocationPoint
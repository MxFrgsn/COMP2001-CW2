from datetime import datetime
import pytz
from config import db, ma

class User(db.Model):
    __tablenmae__ = 'User'
    _table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.Integer, primary_key=True)#

class Trail(db.Model):
    __tablenmae__ = 'Trail'
    _table_args__ = {'schema': 'CW2'}
    table_id = db.Column(db.Integer, primary_key=True)

class Trail_Feature(db.Model):
    __tablenmae__ = 'Trail_Feature'
    _table_args__ = {'schema': 'CW2'}
    #link entity

class Feature(db.Model):
    __tablenmae__ = 'Feature'
    _table_args__ = {'schema': 'CW2'}
    feature_id = db.Column(db.Integer, primary_key=True)

class Location(db.Model):
    __tablenmae__ = 'Location'
    _table_args__ = {'schema': 'CW2'}
    location_id = db.Column(db.Integer, primary_key=True)

    

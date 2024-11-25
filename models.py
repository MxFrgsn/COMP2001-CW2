# models.py
from marshmallow_sqlalchemy import fields
from marshmallow import validates, ValidationError
from config import db, ma

class Location(db.Model): # can i access a valid location from an avaliable database?
    __tablename__ = 'Location'
    __table_args__ = {'schema': 'CW2'}
    location_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String, nullable=False)
    county = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)

    @validates('location_id')
    def validate_location_id(self, value):
        acronym = value.substring(0, 3)
        numbers = value.substring(3, 8)
        if len(value) != 8:
            raise ValidationError('Location ID must be 8 characters long')
        if acronym!= 'LOC':
            raise ValidationError('Location ID must start with LOC')
        if numbers.isdigit() == False:
            raise ValidationError('Location ID must end with 5 numbers')
        return value
    
    @validates('country')
    def validate_country(self, value):
        if len(value) < 3:
            raise ValidationError('Country must be at least 3 characters')
        return value
    
    @validates('county')
    def validate_county(self, value):
        if len(value) < 3:
            raise ValidationError('County must be at least 3 characters')
        return value
    
    @validates('city')
    def validate_city(self, value):
        if len(value) < 3:
            raise ValidationError('City must be at least 3 characters')
        value = round(value, 2)
        return value
class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    trail_id = db.Column(db.String, primary_key=True) 
    location_id = db.Column(db.Integer, db.ForeignKey('CW2.Location.location_id'), nullable=False)  
    owner_id = db.Column(db.String, db.ForeignKey('CW2.User.user_id'), nullable=False)  
    trail_name = db.Column(db.String, nullable=False) 
    summary = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    traffic = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    length = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    elevation_gain = db.Column(db.Integer, nullable=False)
    route_type = db.Column(db.String, nullable=False)

    LOCATION_POINT = 'CW2.Location_Point.location_point_id'
    location_pt_1 = db.Column(db.Integer, db.ForeignKey(LOCATION_POINT))
    location_pt_2 = db.Column(db.Integer, db.ForeignKey(LOCATION_POINT))
    location_pt_3 = db.Column(db.Integer, db.ForeignKey(LOCATION_POINT))
    location_pt_4 = db.Column(db.Integer, db.ForeignKey(LOCATION_POINT))
    location_pt_5 = db.Column(db.Integer, db.ForeignKey(LOCATION_POINT))
    
    @validates('trail_id') 
    def validate_trail_id(self, value):
        acronym = value.substring(0, 3)
        numbers = value.substring(3, 8)
        if len(value) != 8:
            raise ValidationError('Trail ID must be 8 characters long')
        if acronym!= 'TRL':
            raise ValidationError('Trail ID must start with TRL')
        if numbers.isdigit() == False:
            raise ValidationError('Trail ID must end with 5 numbers')
        return value
    
    @validates('trail_name')
    def validate_trail_name(self, value):
        if len(value) < 3:
            raise ValidationError('Trail name must be at least 3 characters')
        if len(value) > 255:
            raise ValidationError('Trail name must be at less than 50 characters')
        return value

    @validates('summary')
    def validate_trail_summary(self, value):
        if len(value) < 50:
            raise ValidationError('Trail summary must be at least 50')
        if len(value) > 255:
            raise ValidationError('Trail summary must be at less than 200 characters')
        return value
    
    @validates('description')
    def validate_trail_description(self, value):
        if len(value) < 100:
            raise ValidationError('Trail description must be at least 100 characters')
        if len(value) > 1500:
            raise ValidationError('Trail description must be at less than 1500 characters') 
        return value 
    
    @validates('traffic')
    def validate_traffic(self, value):
        if value not in ['light', 'moderate', 'heavy']:
            raise ValidationError('Invalid traffic level')
        return value
    
    @validates('difficulty')
    def validate_difficulty(self, value):
        if value not in ['easy', 'moderate', 'hard']:
            raise ValidationError('Invalid difficulty level')
        return value
    
    @validates('length')
    def validate_length(self, value): # Must ensure its in km
        if value < 0.00:
            raise ValidationError('Length must be positive')
        if value > 99999.99:
            raise ValidationError('Length must be less than 99999.99')
        return value

    @validates('duration')
    def validate_duration(self, value):
        hours, minutes = map(int, value.split(':'))
        if hours < 0 or hours > 23:
            raise ValidationError('Hours must be between 00 and 23')
        if minutes < 0 or minutes > 59:
            raise ValidationError('Minutes must be between 00 and 59')
        return value 

    @validates('elevation_gain') # Must ensure its in meters
    def validate_elevation_gain(self, value): 
        if value < 0:
            raise ValidationError('Elevation gain must be positive')
        if value > 9999:
            raise ValidationError('Elevation gain must be less than 9999')
        return value
    
    @validates('route_type')
    def validate_route_type(self, value):
        if value not in ['loop', 'out and back', 'point to point']:
            raise ValidationError('Invalid route type')
        return value
    
class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, nullable=False) 
    password = db.Column(db.String, nullable=False)    
    role = db.Column(db.String, nullable=False)
    
    @validates('user_id')
    def validate_user_id(self, value):
        acronym = value.substring(0, 3)
        numbers = value.substring(3, 8)
        if len(value) != 8:
            raise ValidationError('User ID must be 8 characters long')
        if acronym!= 'USR':
            raise ValidationError('User ID must start with USR')
        if numbers.isdigit() == False:
            raise ValidationError('User ID must end with 5 numbers')
        return value
    
    @validates('username')
    def validate_username(self, value):
        if len(value) < 3:
            raise ValidationError('Username must be at least 3 characters')
        if len(value) > 255:
            raise ValidationError('Username must be at less than 255 characters')
        return value
    
    @validates('email')
    def validate_email(self, value):
        if '@' not in value and '.' not in value:
            raise ValidationError('Invalid email address')
        if len(value) < 3:
            raise ValidationError('Email must be at least 3 characters')
        if len(value) > 255:
            raise ValidationError('Email must be at less than 255 characters')
        return value
    
    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('Password must be at least 8 characters')
        if len(value) > 255:
            raise ValidationError('Password must be at less than 255 characters')
        return value
    
    @validates('role')
    def validate_role(self, value):
        if value not in ['admin', 'user']:
            raise ValidationError('Invalid role')
        return value

class LocationPoint(db.Model):
    __tablename__ = 'Location_Point'
    __table_args__ = {'schema': 'CW2'}
    location_point_id = db.Column(db.Integer, db.ForeignKey('CW2.Location.location_id'), nullable=False, primary_key=True)
    lagitude = db.Column(db.DECIMAL, nullable=False)
    longitude = db.Column(db.DECIMAL, nullable=False)
    description = db.Column(db.String)

    @validates('location_point_id')
    def validate_location_point_id(self, value):
        acronym = value.substring(0, 3)
        numbers = value.substring(3, 8)
        if len(value) != 8:
            raise ValidationError('Location Point ID must be 8 characters long')
        if acronym!= 'LPT':
            raise ValidationError('Location Point ID must start with LPT')
        if numbers.isdigit() == False:
            raise ValidationError('Location Point ID must end with 5 numbers')
        return value
    
    @validates('lagitude')
    def validate_lagitude(self, value):
        if value < -90.00:
            raise ValidationError('Lagitude must be greater than -90.00')
        if value > 90.00:
            raise ValidationError('Lagitude must be less than 90.00')
        return value
    
    @validates('longitude')
    def validate_longitude(self, value):
        if value < -180.00:
            raise ValidationError('Longitude must be greater than -180.00')
        if value > 180.00:
            raise ValidationError('Longitude must be less than 180.00')
        return value
    
    @validates('description')
    def validate_description(self, value):
        if len(value) < 3:
            raise ValidationError('Description must be at least 3 characters')
        if len(value) > 255:
            raise ValidationError('Description must be at less than 255 characters')
        return value
    
class Attraction(db.Model):
    __tablename__ = 'Attraction'
    __table_args__ = {'schema': 'CW2'}
    attraction_id = db.Column(db.String, primary_key=True)
    attraction_name = db.Column(db.String, nullable=False)

    @validates('attraction_id')
    def validate_attraction_id(self, value):
        acronym = value.substring(0, 3)
        numbers = value.substring(3, 8)
        if len(value) != 8:
            raise ValidationError('Attraction ID must be 8 characters long')
        if acronym!= 'ATT':
            raise ValidationError('Attraction ID must start with FET')
        if numbers.isdigit() == False:
            raise ValidationError('Attraction ID must end with 5 numbers')
        return value
    
    @validates('Attraction')
    def validate_Attraction(self, value):
        if len(value) < 3:
            raise ValidationError('Attraction must be at least 3 characters')
        if len(value) > 50:
            raise ValidationError('Attraction must be at less than 50 characters')
        return value
    
class TrailAttraction(db.Model):
    __tablename__ = 'Trail_Attraction'
    __table_args__ = ({'schema': 'CW2'})
    attraction_id = db.Column(db.String, db.ForeignKey('CW2.Attraction.attraction_id'), nullable=False,primary_key=True)
    trail_id = db.Column(db.String, db.ForeignKey('CW2.Trail.trail_id'), nullable=False, primary_key=True)

    Attraction = db.relationship('Attraction', backref=db.backref('trail_attractions', lazy=True))
    trail = db.relationship('Trail', backref=db.backref('trail_attractions', lazy=True))

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
user_schema = UserSchema()
users_schema = UserSchema(many=True)


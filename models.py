# models.py
from marshmallow import fields, validates, ValidationError
from config import db, ma
import re
class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False) 
    email = db.Column(db.String(255), nullable=False) 
    password = db.Column(db.String(255), nullable=False)    
    role = db.Column(db.String(8), nullable=False)

    trail_owner = db.relationship("Trail", back_populates="owner", cascade="all, delete, delete-orphan", lazy="dynamic")

    @validates('username')
    def validate_username(self, value):
        if len(value) < 3:
            raise ValidationError('Username must be at least 3 characters')
        return value
    
    @validates('email')
    def validate_email(self, value):
        if not re.match(r'^[^@]+@[^@]+\.[^@]{2,}$', value):
            raise ValidationError('Invalid email address')
        if len(value) < 3:
            raise ValidationError('Email must be at least 3 characters')
        return value
    
    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('Password must be at least 8 characters')
        if ' ' in value:
            raise ValidationError('Password must not contain spaces.')
        return value
    
    @validates('role')
    def validate_role(self, value):
        if value not in ['admin', 'user']:
            raise ValidationError('Invalid role')
        return value
class TrailLocationPt(db.Model):
    __tablename__ = 'Trail_LocationPt'
    __table_args__ = ({'schema': 'CW2'})
    trail_id = db.Column(db.Integer, db.ForeignKey('CW2.Trail.trail_id'), nullable=False, primary_key=True)
    location_point_id = db.Column(db.Integer, db.ForeignKey('CW2.Location_Point.location_point_id'), nullable=False, primary_key=True)
    order_number = db.Column(db.Integer, nullable=False)
    
    linked_trail_points = db.relationship("Trail", back_populates="trail_location_points")
    linked_location_points = db.relationship("LocationPoint", back_populates="location_points")
    
class TrailAttraction(db.Model):
    __tablename__ = 'Trail_Attraction'
    __table_args__ = ({'schema': 'CW2'})
    attraction_id = db.Column(db.Integer, db.ForeignKey('CW2.Attraction.attraction_id'), nullable=False,primary_key=True)
    trail_id = db.Column(db.Integer, db.ForeignKey('CW2.Trail.trail_id'), nullable=False, primary_key=True)

    trails_attractions_linked = db.relationship("Trail", back_populates="linked_attractions")
    attractions = db.relationship("Attraction", back_populates="attractions_linked")

class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    trail_id = db.Column(db.Integer, primary_key=True) 
    owner_id = db.Column(db.Integer, db.ForeignKey('CW2.User.user_id'), nullable=False)  
    trail_name = db.Column(db.String(255), nullable=False, unique=True) 
    summary = db.Column(db.String(255))
    description = db.Column(db.String(1500))
    location = db.Column(db.String(255), nullable=False)  
    traffic = db.Column(db.String(8), nullable=False) 
    difficulty = db.Column(db.String(8), nullable=False)
    length = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(5), nullable=False)
    elevation_gain = db.Column(db.Integer, nullable=False)
    route_type = db.Column(db.String(14), nullable=False)

    owner = db.relationship("User", back_populates ="trail_owner") 
    linked_attractions = db.relationship("TrailAttraction", back_populates="trails_attractions_linked", cascade="all, delete, delete-orphan")
    trail_location_points = db.relationship("TrailLocationPt", back_populates ="linked_trail_points", cascade="all, delete, delete-orphan",)

    @validates('trail_name')
    def validate_trail_name(self, value):
        if len(value) < 5:
            raise ValidationError('Trail name must be at least 5 characters')
        return value

    @validates('summary')
    def validate_trail_summary(self, value):
        if len(value) < 10 and len(value)!=0:
            raise ValidationError('Trail summary must be at least 50')
        return value
    
    @validates('description')
    def validate_trail_description(self, value):
        if len(value) < 100 and len(value)!=0:
            raise ValidationError('Trail description must be at least 100 characters')
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
        value = round(value, 2)
        if value < 0.00:
            raise ValidationError('Length must be positive')
        if value > 99999.99:
            raise ValidationError('Length must be less than 99999.99')
        return value

    @validates('duration')
    def validate_duration(self, value):
        try:
            hours, minutes = map(int, value.split(':'))
        except ValueError:
            raise ValidationError("Duration must be in the format 'hh:mm'.")
        if hours < 0 or hours > 99:
            raise ValidationError('Hours must be between 00 and 99.')
        if minutes < 0 or minutes > 59:
            raise ValidationError('Minutes must be between 00 and 59.')
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

class LocationPoint(db.Model):
    __tablename__ = 'Location_Point'
    __table_args__ = {'schema': 'CW2'}
    location_point_id = db.Column(db.Integer, nullable=False, primary_key=True)
    latitude = db.Column(db.DECIMAL(precision=9, scale=6), nullable=False)
    longitude = db.Column(db.DECIMAL(precision=9, scale=6), nullable=False)
    description = db.Column(db.String(255))

    location_points = db.relationship("TrailLocationPt", back_populates="linked_location_points", cascade="all, delete, delete-orphan", lazy="dynamic")
    
    @validates('latitude')
    def validate_latitude(self, value):
        if not (-90.0 <= value <= 90.0):
            raise ValidationError('Latitude must be between -90.00 and 90.00')
        return value
    
    @validates('longitude')
    def validate_longitude(self, value):
        if not (-180.0 <= value <= 180.0):
            raise ValidationError('Longitude must be between -180.00 and 180.00')
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
    attraction_id = db.Column(db.Integer, primary_key=True)
    attraction_name = db.Column(db.String(255), nullable=False)

    attractions_linked = db.relationship("TrailAttraction", back_populates="attractions", cascade="all, delete, delete-orphan", lazy="dynamic")

    @validates('Attraction')
    def validate_Attraction(self, value):
        if len(value) < 3:
            raise ValidationError('Attraction must be at least 3 characters')
        return value
class TrailSchema(ma.SQLAlchemyAutoSchema):
    trail_id = fields.Integer()
    trail_name = fields.String()
    summary = fields.String()
    description = fields.String()
    location = fields.String()
    difficulty = fields.String()
    length = fields.Float()
    traffic = fields.String()
    duration = fields.String()
    elevation_gain = fields.Integer()  
    route_type = fields.String()  
    owner_id = fields.Integer()
    owner = fields.Nested('UserSchema')
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        exclude = ['owner.user_id']

class LimitedTrailSchema(ma.SQLAlchemyAutoSchema):
    trail_name = fields.String()
    summary = fields.String()
    description = fields.String()
    location = fields.String()
    difficulty = fields.String()
    length = fields.Float()
    traffic = fields.String()
    duration = fields.String()
    elevation_gain = fields.Integer()  
    route_type = fields.String()  
    owner_id = fields.Integer()
    owner = fields.Nested('UserSchema')
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        exclude = ['trail_id', 'owner.user_id','owner.email', 'owner.password', 'owner.role']

class UserSchema(ma.SQLAlchemyAutoSchema):
    user_id = fields.Integer()
    username = fields.String()
    email = fields.String()
    password = fields.String()
    role = fields.String()
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

class LimitedUserSchema(ma.SQLAlchemyAutoSchema):
    user_id = fields.Integer()
    username = fields.String()
    role = fields.String()
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        exclude = ['email', 'password']
class LocationPointSchema(ma.SQLAlchemyAutoSchema):
    location_point_id = fields.Integer()
    latitude = fields.Float()
    longitude = fields.Float()
    description = fields.String()
    class Meta:
        model = LocationPoint
        load_instance = True
        sqla_session = db.session
class AttractionSchema(ma.SQLAlchemyAutoSchema):
    attraction_id = fields.Integer()
    attraction_name = fields.String()
    class Meta:
        model = Attraction
        load_instance = True
        sqla_session = db.session

class TrailAttractionSchema(ma.SQLAlchemyAutoSchema):
    attraction_id = fields.Integer()
    trail_id = fields.Integer()
    class Meta:
        model = TrailAttraction
        load_instance = True
        sqla_session = db.session

class TrailLocationPtSchema(ma.SQLAlchemyAutoSchema):
    trail_id = fields.Integer()
    location_point_id = fields.Integer()
    order_number = fields.Integer()
    class Meta:
        model = TrailLocationPt
        load_instance = True
        sqla_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)

limited_trail_schema = LimitedTrailSchema()
limited_trails_schema = LimitedTrailSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

location_point_schema = LocationPointSchema()
location_points_schema = LocationPointSchema(many=True)

attraction_schema = AttractionSchema()
attractions_schema = AttractionSchema(many=True)

trail_attraction_schema = TrailAttractionSchema()
trail_attractions_schema = TrailAttractionSchema(many=True)

trail_locationpt_schema = TrailLocationPtSchema()
trail_locationpts_schema = TrailLocationPtSchema(many=True)

limited_user_schema = LimitedUserSchema()
limited_users_schema = LimitedUserSchema(many=True)


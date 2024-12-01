# models.py
from marshmallow import fields
from marshmallow import validates, ValidationError
from config import db, ma
class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    trail_id = db.Column(db.String(8), primary_key=True) 
    owner_id = db.Column(db.String(8), db.ForeignKey('CW2.User.user_id'), nullable=False)  
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

    LOCATION_POINT = 'CW2.Location_Point.location_point_id'
    location_pt_1 = db.Column(db.String(8), db.ForeignKey(LOCATION_POINT))
    location_pt_2 = db.Column(db.String(8), db.ForeignKey(LOCATION_POINT))
    location_pt_3 = db.Column(db.String(8), db.ForeignKey(LOCATION_POINT))
    location_pt_4 = db.Column(db.String(8), db.ForeignKey(LOCATION_POINT))
    location_pt_5 = db.Column(db.String(8), db.ForeignKey(LOCATION_POINT))

    owner = db.relationship("User", backref="trails")
    location_point_1 = db.relationship("LocationPoint", foreign_keys=[location_pt_1])
    location_point_2 = db.relationship("LocationPoint", foreign_keys=[location_pt_2])
    location_point_3 = db.relationship("LocationPoint", foreign_keys=[location_pt_3])
    location_point_4 = db.relationship("LocationPoint", foreign_keys=[location_pt_4])
    location_point_5 = db.relationship("LocationPoint", foreign_keys=[location_pt_5])
    
    @validates('trail_id') 
    def validate_trail_id(self, value):
        acronym = value[0:3]
        numbers = value[3:8]
        if len(value) != 8:
            raise ValidationError('Trail ID must be 8 characters long')
        if acronym!= 'TRL':
            raise ValidationError('Trail ID must start with TRL')
        if numbers.isdigit() == False:
            raise ValidationError('Trail ID must end with 5 numbers')
        return value
    
    @validates('trail_name')
    def validate_trail_name(self, value):
        if len(value) < 5:
            raise ValidationError('Trail name must be at least 3 characters')
        return value

    @validates('summary')
    def validate_trail_summary(self, value):
        if len(value) < 10 & len(value)!=0:
            raise ValidationError('Trail summary must be at least 50')
        return value
    
    @validates('description')
    def validate_trail_description(self, value):
        if len(value) < 100 & len(value)!=0:
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
    
class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.String(8), primary_key=True)
    username = db.Column(db.String(255), nullable=False) 
    email = db.Column(db.String(255), nullable=False) 
    password = db.Column(db.String(255), nullable=False)    
    role = db.Column(db.String(8), nullable=False)
    
    @validates('user_id')
    def validate_user_id(self, value):
        acronym = value[0:3]
        numbers = value[3:8]
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
        return value
    
    @validates('email')
    def validate_email(self, value):
        if '@' not in value and '.' not in value:
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

class LocationPoint(db.Model):
    __tablename__ = 'Location_Point'
    __table_args__ = {'schema': 'CW2'}
    location_point_id = db.Column(db.String(8), nullable=False, primary_key=True)
    latitude = db.Column(db.DECIMAL(precision=9, scale=6), nullable=False)
    longitude = db.Column(db.DECIMAL(precision=9, scale=6), nullable=False)
    description = db.Column(db.String(255))

    @validates('location_point_id')
    def validate_location_point_id(self, value):
        acronym = value[0:3]
        numbers = value[3:8]
        if len(value) != 8:
            raise ValidationError('Location Point ID must be 8 characters long')
        if acronym!= 'LPT':
            raise ValidationError('Location Point ID must start with LPT')
        if numbers.isdigit() == False:
            raise ValidationError('Location Point ID must end with 5 numbers')
        return value
    
    @validates('lagitude')
    def validate_lagitude(self, value):
        if not (-90.0 <= value <= 90.0):
            raise ValidationError('Latitude must be between -90.00 and 90.00')
        if len(str(value).split(".")[1]) > 6:
            raise ValidationError('Latitude must have at most 6 decimal places')
        return value

    @validates('longitude')
    def validate_longitude(self, value):
        if not (-180.0 <= value <= 180.0):
            raise ValidationError('Longitude must be between -180.00 and 180.00')
        if len(str(value).split(".")[1]) > 6:
            raise ValidationError('Longitude must have at most 6 decimal places')
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
    attraction_id = db.Column(db.String(8), primary_key=True)
    attraction_name = db.Column(db.String(255), nullable=False)

    @validates('attraction_id')
    def validate_attraction_id(self, value):
        acronym = value[0:3]
        numbers = value[3:8]
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
        return value
    
class TrailAttraction(db.Model):
    __tablename__ = 'Trail_Attraction'
    __table_args__ = ({'schema': 'CW2'})
    attraction_id = db.Column(db.String(8), db.ForeignKey('CW2.Attraction.attraction_id'), nullable=False,primary_key=True)
    trail_id = db.Column(db.String(8), db.ForeignKey('CW2.Trail.trail_id'), nullable=False, primary_key=True)

    Attraction = db.relationship('Attraction', backref='trail_attractions')
    Trail = db.relationship('Trail', backref= 'trail_attractions')

class TrailSchema(ma.SQLAlchemyAutoSchema):
    trail_id = fields.Str(required=True)
    trail_name = fields.Str(required=True)
    summary = fields.Str(missing=None)
    description = fields.Str(missing=None)
    location = fields.Str(required=True)
    difficulty = fields.Str(required=True)
    length = fields.Float(required=True)
    traffic = fields.Str(required=True)
    duration = fields.Str(missing=None)
    elevation_gain = fields.Integer(missing=None)  
    route_type = fields.Str(missing=None)  
    owner_id = fields.Str(required=True)
    location_pt_1 = fields.Str()
    location_pt_2 = fields.Str()
    location_pt_3 = fields.Str()
    location_pt_4 = fields.Str()
    location_pt_5 = fields.Str()
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
class UserSchema(ma.SQLAlchemyAutoSchema):
    user_id = fields.Str()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    role = fields.Str()
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class LocationPointSchema(ma.SQLAlchemyAutoSchema):
    location_point_id = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    description = fields.Str()
    class Meta:
        model = LocationPoint
        load_instance = True
        sqla_session = db.session

location_point_schema = LocationPointSchema()
location_points_schema = LocationPointSchema(many=True)

class AttractionSchema(ma.SQLAlchemyAutoSchema):
    attraction_id = fields.Str()
    attraction_name = fields.Str()
    class Meta:
        model = Attraction
        load_instance = True
        sqla_session = db.session

attraction_schema = AttractionSchema()
attractions_schema = AttractionSchema(many=True)

class TrailAttractionSchema(ma.SQLAlchemyAutoSchema):
    attraction_id = fields.Str()
    trail_id = fields.Str()
    class Meta:
        model = TrailAttraction
        load_instance = True
        sqla_session = db.session

trail_attraction_schema = TrailAttractionSchema()
trail_attractions_schema = TrailAttractionSchema(many=True)

# models.py
from marshmallow_sqlalchemy import fields
from marshmallow import validates, ValidationError
from config import db, ma

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, nullable=False) 
    password = db.Column(db.String, nullable=False)    
    
    @validates('email')
    def validate_email(self, value):
        if '@' not in value:
            raise ValidationError('Invalid email address')
        return value
    
    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('Password must be at least 8 characters')
        return value

class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    trail_id = db.Column(db.String, primary_key=True)  # needs validation, same for user id, location id and Attraction id 
    trail_name = db.Column(db.String, nullable=False) 
    trail_summary = db.Column(db.String, nullable=False)
    trail_description = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    traffic = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('CW2.Location.location_id'), nullable=False)  
    length = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    route_type = db.Column(db.String, nullable=False)

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
        if len(value) < 50:
            raise ValidationError('Trail name must be at least 3 characters')
        return value

    @validates('trail_summary')
    def validate_trail_summary(self, value):
        if len(value) < 100:
            raise ValidationError('Trail summary must be at least 50 characters')
        return value
    
    @validates('trail_description')
    def validate_trail_description(self, value):
        if len(value) < 100:
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
    def validate_length(self, value):
        if value < 0:
            raise ValidationError('Length must be positive')
        return value

    @validates('duration')
    def validate_duration(self, value):
        if value < 0:
            raise ValidationError('Duration must be positive')
        return value

    @validates('route_type')
    def validate_route_type(self, value):
        if value not in ['loop', 'out and back', 'point to point']:
            raise ValidationError('Invalid route type')
        return value
    

class Trail_Ownership(db.Model):
    __tablename__ = 'Trail_Ownership'
    __table_args__ = ({'schema': 'CW2'})
    user_id = db.Column(db.String, db.ForeignKey('CW2.User.user_id'), nullable=False, primary_key=True)
    trail_id = db.Column(db.String, db.ForeignKey('CW2.Trail.trail_id'), nullable=False,primary_key=True)

    user = db.relationship('User', backref=db.backref('owned_trails', lazy=True))
    trail = db.relationship('Trail', backref=db.backref('trail_owners', lazy=True))

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
        if acronym!= 'TRL':
            raise ValidationError('Attraction ID must start with FET')
        if numbers.isdigit() == False:
            raise ValidationError('Attraction ID must end with 5 numbers')
        return value
    
    @validates('Attraction')
    def validate_Attraction(self, value):
        if len(value) < 3:
            raise ValidationError('Attraction must be at least 3 characters')
        return value
    
class Trail_Attraction(db.Model):
    __tablename__ = 'Trail_Attraction'
    __table_args__ = ({'schema': 'CW2'})
    attraction_id = db.Column(db.String, db.ForeignKey('CW2.Attraction.attraction_id'), nullable=False,primary_key=True)
    trail_id = db.Column(db.String, db.ForeignKey('CW2.Trail.trail_id'), nullable=False, primary_key=True)

    Attraction = db.relationship('Attraction', backref=db.backref('trail_attractions', lazy=True))
    trail = db.relationship('Trail', backref=db.backref('trail_attractions', lazy=True))

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
        if acronym!= 'TRL':
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
        return value

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session

class TrailOwnershipSchema(ma.SQLAlchemyAutoSchema):
    owner = fields.Nested(UserSchema)  
    class Meta:
        model = Trail_Ownership
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many=True)

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)

trail_ownership_schema = TrailOwnershipSchema()
trail_ownerships_schema = TrailOwnershipSchema(many=True)


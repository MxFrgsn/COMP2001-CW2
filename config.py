# config.py
import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_session import Session

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app  

app.config['SQLALCHEMY_DATABASE_URI'] = ('mssql+pyodbc:///?odbc_connect='
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DIST-6-505.uopnet.plymouth.ac.uk;'
    'DATABASE=COMP2001_MFerguson;'
    'UID=MFerguson;'
    'PWD=GjiF140*;'
    'Encrypt=Yes;'
    'TrustServerCertificate=Yes;'
)
app.config['SECRET_KEY'] = 'secret_key'  # Replace with a secure random key
app.config['SESSION_TYPE'] = 'filesystem'  # Use server-side sessions
app.config['SESSION_COOKIE_SECURE'] = True  # Use HTTPS in production
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Prevent CSRF attacks
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Session(app)

db = SQLAlchemy(app)
ma = Marshmallow(app) 
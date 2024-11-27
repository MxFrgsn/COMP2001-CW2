# app.py
from flask import render_template
import config
from models import Trail

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 

@app.route('/')
def home():
    return render_template('home.html', trails = Trail.query.all())

if __name__ == '__main__': 
    # dont need to when using web server 
    # need to use web server /auth/api/users
    app.run(host='0.0.0.0',port=8000,debug=True)


# need to comment current code
# need to ensure im using my web.socem.plymouth.ac.uk web server not my local one

# create sql trigger or python function to ensure IDs for each table are unique automatically!!!

# create CRUD for all tables 
    # location points
    # attractions
    # do query to search trails by name, location, dfifficulty, traffic, -> maybe a range if included? length duration, elevation gain, route type, 
    # could also do attraction id, owner id 
    # o Error checking for how far apart locations is out of scope
    # when using trail_attractions, can view attraction description
    # query for other tables
    # use authentication API: https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users 


# IIS Web Server
# Your web page is available at:
# http://cent-5-534.uopnet.plymouth.ac.uk/COMP2001/MFerguson
# https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users

# IIS Web Server File Share:
# Connect using file explorer.  
# Login with univeristy email and password.
# \\CENT-5-534.uopnet.plymouth.ac.uk\COMP2001\MFerguson 

# MS SQL Server 
# The host URL is: DIST-6-505.uopnet.plymouth.ac.uk 
# Your Database is: COMP2001_MFerguson
# Your Username is:MFerguson
# Your Password is: GjiF140*

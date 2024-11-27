# app.py
from flask import render_template
import config
from models import Trail

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 

@app.route('/')
def home():
    return render_template('home.html', trails = Trail.query.all())

if __name__ == '__main__': # dont need to when using web server 
    # need to use web server /auth/api/users
    app.run(host='0.0.0.0',port=8000,debug=True)

# need to comment current code
# need to ensure im using my web.socem.plymouth.ac.uk web server not my local one

# create sql trigger or python function to ensure IDs for each table are unique automatically!!!

# should i specify the length of every string in models.py?
# create CRUD for all tables 
    # dont need to do this for attractions as its linked to trail and predefined in the database, maybe retrieve for the tables but thats it.
    # i dont think i need to do this for location points either not sure 
    # do need to do it for trail attraction, trail and user and location point.

    # currently doing trails -> need to do swagger, test and other functions
    # could search or sort by location or attraction or owner id or trail name instead of just trail_id 


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

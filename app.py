# app.py
from flask import render_template
import config
from models import Trail

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=8000,debug=True)



# OVERALL:
# here are several parts to the micro-service that you will need to create
# • Protect against OWASP Top 10 vulnerabilities where possible -> need to add authentication to the API, done sql injection with sql alchemy
# • Must ensure it is RESTful 

    # SPECIFIC:
    # need to comment current code
    # write readme file
    # should i be able to view trails based on the name or user id of the trail owner? -> doable using query in read_all function 
    # but need to link tables in swagger and when dumping the data from the schema.

    # should i be able to view the attractions of a trail? in the read_one/read_all function? 
    # should add a function to view what users a user owns in user.py? 
    # should i add a update to trail_attraction.py and attractions.py?
    # need to add crud stored procedures to the sql database for each table!!!


    # do query to search trails by name, location, dfifficulty, traffic, -> maybe a range if included? length duration, elevation gain, route type, 
    # could also do attraction id, owner id 
    # IF IM DOING THIS, WHY DO I NEED THE READ_ONE FUNCTION????

    # o Error checking for how far apart locations is out of scope

    # when using trail_attractions, can view attraction description
    # query for other tables
    # create sql trigger or python function to ensure IDs for each table are unique automatically!!!
    # need to ensure im using my web.socem.plymouth.ac.uk web server not my local one
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

# Docker Image: mxfrgsn/comp2001_cw2
# GitHub Repository: https://github.com/MxFrgsn/COMP2001-CW2
# docker run -p 8000:8000 mxfrgsn/comp2001_cw2

# app.py
from flask import session
import config
from models import Trail

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 

@app.route("/")
def redirect_to_swagger():
    session['user_id'] = 1 # sets default user to admin
    session['role'] = 'admin' # sets default role to admin
    return "<meta http-equiv='refresh' content='0; url=/api/ui/'>"

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=8000,debug=True)


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
# Your Username is: MFerguson
# Your Password is: GjiF140*

# GitHub Repository: https://github.com/MxFrgsn/COMP2001-CW2
# Docker Image: mxfrgsn/comp2001_cw2
# docker pull mxfrgsn/comp2001_cw2
# docker run -p 8000:8000 mxfrgsn/comp2001_cw2

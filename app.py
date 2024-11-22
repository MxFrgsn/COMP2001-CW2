# app.py
from flask import Flask, render_template
import config
from models import Trail

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 
@app.route('/')

def home():
    return render_template('home.html', trails = Trail.query.all())

if __name__ == '__main__': # dontneed this apparently?
    app.run(host='0.0.0.0',port=8000,debug=True)

# need to comment current code
# need to ensure im using my web.socem.plymouth.ac.uk web server
# neeed to make theses files are in file share web server -> not sure what log in details are
# create a database with tables for countries, counties and cities -> or find online database
# create sql trigger or python function to ensure IDs for each table are unique automatically

""" 
IIS Web Server
Your web page is available at:
http://cent-5-534.uopnet.plymouth.ac.uk/COMP2001/MFerguson
https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users

Web server file share:
Connect using file explorer.  
Login with UOPNET\MFerguson
\\CENT-5-534.uopnet.plymouth.ac.uk\COMP2001\MFerguson 

MS SQL Server 
The host URL is: DIST-6-505.uopnet.plymouth.ac.uk 
Your Database is: COMP2001_MFerguson
Your Username is:MFerguson
Your Password is: GjiF140*
"""
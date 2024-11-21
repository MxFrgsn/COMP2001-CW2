# app.py
from flask import Flask, render_template
import config
from models import User,Location, Trail, Attraction, Trail_Attraction, Trail_Ownership

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 
@app.route('/')

def home():
    return render_template('home.html', trails = Trail.query.all())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)

# need to comment current code
# now run notebook for sql code
# then test app.py -> see if works and then work on trail.py and swagger.yml in tandem
# create sql trigger or python function to ensure IDs for each table are unique automatically
# find out if theres online databaes to go through countries,counties and cities as locations.
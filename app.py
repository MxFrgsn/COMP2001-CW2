# app.py
from flask import Flask, render_template
import config
from models import User, Trail, Trail_Attraction, Attraction, Location

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 
@app.route('/')

def home():
    return render_template('home.html', trails = Trail.query.all())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)

# need to go through models.py and ensure validation is correct 
# and convert to sql in sql.ipynb
# need to comment current code
# include validation to ensure its in time format HH:MM in models.py
# create sql trigger or python function to ensure IDs for each table are unique automatically

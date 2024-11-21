from flask import Flask, render_template
import config
from models import User, Trail, Trail_Feature, Feature, Location

app = config.connex_app
app.add_api(config.basedir / 'swagger.yml') 
@app.route('/')

def home():
    return render_template('home.html', trails = Trail.query.all())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
#################
#### imports ####
#################
import os
from flask import Flask
from flask import request, g, redirect, url_for
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_mail import Mail

##babel

from flask_babel import Babel

# local imports
from config import app_config



################
#### config ####
################
config_name = os.getenv('FLASK_ENV', 'development')
template_dir = os.path.abspath('src/app/templates')

app = Flask(__name__, instance_relative_config=True, template_folder=template_dir)
app.config.from_object(app_config[config_name])

bcrypt = Bcrypt(app)


db = SQLAlchemy(app)
ma = Marshmallow(app)

mail = Mail(app)


####BABEL
babel = Babel(app)

@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code

@app.route('/')
def home():
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return redirect(url_for('multilingual.index'))

####BABEL

def create_app():
        
    #from app.route.home.views import bphome
    #app.register_blueprint(bphome)
    #db.init_app(app)
    #ma.init_app(app)

    from app.route.multilingual import bpmultilingual
    app.register_blueprint(bpmultilingual)

    
    
    return app


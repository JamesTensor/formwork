#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,static_url_path='',static_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sql'),
    )

    #app.config.from_object('settings')
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    from . import database, routes, services
    database.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    
    return app
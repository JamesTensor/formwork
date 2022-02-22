#coding=utf-8
from . import database 

def init_app(app):
    database.init_app(app)  
    
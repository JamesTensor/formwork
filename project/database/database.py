#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))
import threading

from flask import current_app, g
from flask.cli import with_appcontext

from . import pysql
from . import pysql_config as p_c

def init_db():
    try:
        p_c.db = pysql.MYSQL(p_c.HOST,p_c.USERNAME,p_c.PASSWORD,p_c.DATABASE,p_c.PORT)
        print("connect sql successfully")
        return p_c.db
    except Exception as e:
        print(e)
        print("connect sql failed")
        return False

def init_app(app):
    formwork = threading.Thread(target=init_db, args=())
    formwork.start()
    
    
        
        
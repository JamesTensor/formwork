#coding=utf-8
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))

import functools,os,datetime,random,string,json

import requests

from flask import (
    Blueprint,flash,g,redirect,render_template,request,session, url_for,current_app,jsonify,abort,send_from_directory
)
from jinja2 import TemplateNotFound
from werkzeug.security import check_password_hash, generate_password_hash

from ..services import third_function as t_f_m
t_f = t_f_m.third_function()
third_function = t_f
from ..services import third_object as t_o_m
t_o = t_o_m.third_object()
third_object = t_o
from ..database import pysql_config as p_c
from ..database import sql as s

indexbp = Blueprint('', __name__,url_prefix='/')    

@indexbp.route('/init', methods=('GET', 'POST'))
def init():
    global record
    try:
        record = p_c.db.ExecQuery(s.t["test_sql"])    
    except Exception as e:
        record = (('error', 'error in record', '0.0'),)
    return "inited"

#set up icon
@indexbp.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('favicon.ico')
            
@indexbp.route('/', methods=('GET', 'POST'))
def index():
    getpostdict = t_f.s_r(request)
    g_p_d = getpostdict
    #print(g_p_d)
    #return render_template('index.html',name="formwork index")
    return "hello framework flask"

@indexbp.route('/test/formwork', methods=('GET', 'POST'))
def test_formwork():
    getpostdict = t_f.s_r(request)
    g_p_d = getpostdict
    serial = t_f.g_s()
    g_p_d['serial'] = serial
    g_p_d['ip'] = request.remote_addr
    g_p_d['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print( p_c.db.secure(g_p_d['key']) )
    p_c.db.ExecNonQuery(s.t["formwork_sql"].format(formwork=p_c.db.secure(g_p_d['formwork'])))
    return render_template('formwork.html',formwork=formwork)
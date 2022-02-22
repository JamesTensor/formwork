#coding=utf-8
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))
import functools,os

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

adminbp = Blueprint('admin', __name__,url_prefix='/admin')

def admin_login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.username is None:
            return redirect("/admin/")
        return view(**kwargs)
    return wrapped_view
    
@adminbp.route('/admin', methods=('GET', 'POST'))
@admin_login_required
def admin():
    return render_template('admin.html',name="formwork admin web") 

@adminbp.route('/data', methods=('GET', 'POST'))
@admin_login_required
def data():
    #admin_sql_data =  p_c.db.ExecQueryDict(s.t["select_admin_sql"])  
    #print(admin_sql_data)
    admin_data = {"name":"formwork"}
    #admin_data["data"] = list(admin_sql_data)
    return jsonify(admin_data)

@adminbp.route('/', methods=('GET', 'POST'))
def admin_login():
    return render_template('adminlogin.html',name="formwork admin_login web")

    

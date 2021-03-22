from models import *

from flask import Blueprint, render_template, request, redirect, session


bp = Blueprint('login', __name__ )



@bp.route('/', methods=['GET'])
def Get():
    msg = request.args.get('msg', None)
    return render_template('login/login.html', msg = msg)
    
    
@bp.route('/', methods=['POST'])
def Check():
    _username =  request.form['username']
    _password = request.form['password']
    
    a = Users.get_or_none(_username == Users.username)
    
    if a == None:
        return redirect('/login/?msg=Такой пользователь остуствует')
        
    if _password != a.password:
        return redirect('/login/?msg=Неправильный пароль')
    
    
    session['username'] = a.username
    session['role'] = a.role
    
    if a.role == 'admin':
        return redirect('/admin/')
    else:
        return redirect('/pharm')
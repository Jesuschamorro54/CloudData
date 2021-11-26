from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash, jsonify, abort, g
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import functools
from datetime import datetime, timedelta, date

main = blueprints.Blueprint('main', __name__)


def login_required(view):
    @functools.wraps(view)
    def wraped_view(**kwargs):
        if 'usr_email' not in session:
            return redirect(url_for('main.login'))
        return view(**kwargs)   
    return wraped_view

@main.route('/logout/')
def logout():
   session.clear()
   return redirect(url_for('main.login'))

@main.route('/login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        usr_email = request.form['usr_email']
        usr_password = request.form['usr_password']
        if(usr_email =='jesusfeli54@gmail.com' and usr_password =='1234'):
            session['id'] = 1
            session['usr_name'] = 'Jesus'
            session['usr_email'] = 'jesusfeli54@gmail.com'
            session['usr_rol'] = 'admin'
            session['acc'] = True
            return redirect(url_for('main.index'))

    return render_template('login.html')

@main.context_processor
def login_acc():
    if 'acc' in session:
        return {'is_login':True}
    else:
        return {'is_login':False}

@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/sign-in/')
def register():
    return render_template('sign_in.html')
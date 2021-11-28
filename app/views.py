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

@main.route('/sign-in/')
def register():
    return render_template('sign_in.html')

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
            session['usr_name'] = 'Jesus Chamorro'
            session['usr_email'] = 'jesusfeli54@gmail.com'
            session['usr_rol'] = 'admin'
            session['acc'] = True
            return redirect(url_for('main.index'))

    return render_template('login.html')

@main.context_processor
def login_acc():
    if 'acc' in session:
        is_rol = session.get('usr_rol')
        g.is_admin = True if is_rol=='admin'else False
        g.is_moder = True if is_rol=='moderador' else False
        g.is_free = True if is_rol=='free' else False
        return {'is_login':True}
    else:
        return {'is_login':False}

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/registros')
@login_required
def registros():
    is_rol = session.get('usr_rol')
    g.is_admin = True if is_rol=='admin'else False
    g.is_moder = True if is_rol=='moderador' else False
    g.is_free = True if is_rol=='free' else False

    info = [
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
        ['1002159985', 'Jesus felipe', 19, '2002-30-06', 'Normal', 'Masculino', '3002181326', 'normal', '32823914', 'Hortencia', '55', 'Los sueños'],
    ]
    return render_template('registros.html', reserva_list = info)


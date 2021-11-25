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


@main.route('/',)
def index():
    return render_template('index.html')


@main.route('/login/')
def login():
    return render_template('login.html')

@main.route('/sign-in/')
def register():
    return render_template('sign_in.html')
from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash, jsonify, abort, g
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import functools
import json

main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():   
    return render_template('index.html')
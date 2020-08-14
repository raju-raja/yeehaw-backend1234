import os
import json
import flask
import flask_cors
# import flask_sqlalchemy
import datetime

from flask import Flask, request, jsonify, session,make_response, current_app, render_template, json
from flask_cors import CORS, cross_origin
# from flask_sqlalchemy import SQLAlchemy

# initializes app
app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

# initializes database
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')

app.config.from_object(__name__)

CORS(app)

@app.route("/") 
def home_view(): 
		return "hey friends"


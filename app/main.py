from flask import Flask 
import flask_cors
from flask_cors import CORS, cross_origin

app = Flask(__name__) 



@app.route("/") 
def home_view(): 
		return "hey friends"


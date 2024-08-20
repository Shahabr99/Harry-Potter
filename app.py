from flask import Flask
import os
from dotenv import load_dotenv
from models import db, connect_db


app = Flask(__name__)

# load variable from .env file
load_dotenv()

# access the environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', 'postgresql:///HarryPotter')

connect_db(app)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret!')
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://mongo:27017/chatapp')

mongo = PyMongo(app)
socketio = SocketIO(app)

from app import routes, socket_events
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
import socket
socket.getaddrinfo('localhost', 8080)


app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'stmp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ulusoyeminn@gmail.com'
app.config['MAIL_PASSWORD'] = 'emin326159487'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)

from CLEANBLOG import routes
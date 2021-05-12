from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Root@"
app.config["SECRET_KEY"] = os.getenv("SECRET")

db = SQLAlchemy(app)

from application import routes

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jrjrqlznydduow:Ydcaj6hw2OJIyMU7Os0Kcy5lDo@ec2-107-21-100-118.compute-1.amazonaws.com:5432/d5i7p4d102h8ad'                                      db= SQLAlchemy(app)
 
from app import views, models

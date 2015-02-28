from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lcjsohpzwnnvqo:_hdakVe7QefNX9jfJd9R-AvceA@ec2-23-21-231-14.compute-1.amazonaws.com:5432/d318k172garutn'                                         
db= SQLAlchemy(app)

 
from app import views, models

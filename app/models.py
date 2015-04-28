from . import db
import json
from marshmallow import Schema, fields, pprint

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image=db.Column(db.String(200))
  firstname=db.Column(db.String(80))
  lastname=db.Column(db.String(80))
  sex=db.Column(db.String(120))
  age= db.Column(db.Integer)
  username = db.Column(db.String(30))
  email = db.Column(db.String(50))
  password = db.Column(db.String(15))

  def __init__(self,image,firstname,lastname,sex,age,username,email, password):
      self.image=image
      self.firstname = firstname
      self.lastname = lastname
      self.sex = sex
      self.age = age
      self.username = username 
      self.email = email 
      self.password = password
      
  def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  
  def __repr__(self):
    return'<User%r>'%self.firstname

 
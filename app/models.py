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

  def __init__(self,image,firstname,lastname,sex,age):
      self.image=image
      self.firstname = firstname
      self.lastname = lastname
      self.sex = sex
      self.age = age
      
  def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  
  def __repr__(self):
    return'<User%r>'%self.firstname

 
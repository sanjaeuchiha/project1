"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
import sys
import json
from app import db
from app.models import User
from app import app
from flask import render_template, request, redirect, url_for, jsonify



###
# Routing for your application.
###

@app.route('/games')
def home():
    """Render website's home page."""
    return render_template('gameshome.html')
  
  
@app.route('/signup', methods =['GET', 'POST'])
def signup():
  if request.method == "POST":
    filefolder ='./app/static/img'
    image = request.files['image']
    imagename = image.filename
    image.save(os.path.join(filefolder,imagename))
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    sex = request.form['sex']
    age =  request.form['age']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    entry=User(os.path.join(filefolder,imagename),firstname,lastname,sex,age,username,email,password)
    db.session.add(entry)
    db.session.commit()    
  return render_template("signup.html")

@app.route('/login', methods =['GET','POST'])
def login():
  if request.method =="POST":
    fusername = request.form['username']
    fpassword = request.form['password']
    duser = db.session.query(User).filter(User.username==fusername).one()
    if fusername == duser.username and fpassword == duser.password:
      return redirect("http://info-3180-lab-1-189038.use1.nitrousbox.com:8080/games")
  return render_template("login.html")
  

@app.route('/person')
def person():
  first_user=db.session.query(User).first()
  return "image:{},firstname:{}, lastname{}, sex:{}, age:{}, username{}, email{}".format(first_user.image,first_user.firstname, first_user.lastname , first_user.sex, first_user.age, first_user.username, first_user.email)

@app.route('/profiles', methods =["POST", "GET"])
def viewprofiles():
  results = db.session.query(User).all()
  profile_list = []
  for result in results:
    profile_list.append({'UserID' : result.id,
                         'Photo' : result.image,
                         'Firstname' : result.firstname,
                         'Lastname' : result.lastname,
                         'Sex' : result.sex,
                         'Age' : result.age,
                         'Username' : result.username,
                         'email' : result.email})
  return jsonify(users=profile_list)

  
@app.route("/profiles/<userid>")
def viewprofile(userid):
  entry = User.query.filter_by(id=userid).one()
  fentry = User.as_dict(entry)
  return jsonify(User=fentry)



@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

  
  

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")

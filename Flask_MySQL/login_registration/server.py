from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt (app)
mysql = MySQLConnector(app,'login_registration')
app.secret_key="secret"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template ('index.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pw_confirm = request.form['pw_confirm']
    pw_hash = bcrypt.generate_password_hash(password) #generate hash to insert into db
    print "got registration info"
    errors = True
    if len(first_name)<2:
        flash ("First name must be at least 2 characters")
        errors = False
    elif not NAME_REGEX.match(first_name):
        flash ("First name can be only letters")
        errors = False
    if len(last_name)<2:
        flash ("Last name must be at least 2 characters")
        errors = False
    elif not NAME_REGEX.match(last_name):
        flash ("Last name can be only letters")
        errors = False
    if len(email)<1:
        flash("Email field cannot be empty")
        errors = False
    elif not EMAIL_REGEX.match(email):
        flash("Email is not valid")
        errors = False
    if len(password)<8:
        flash("Password must be at least 8 characters")
        errors = False
    if (pw_confirm != password):
        flash("Passwords must match")
        errors = False
    if errors == True:
        flash ("Success! Please login")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password);"
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": pw_hash
        }
        mysql.query_db(query, data)
        print "user added"
        return redirect('/')
    else:
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        'email': email
    }
    user = mysql.query_db(query, data) #array
    print user
    print "got login info"
    errors = False
    if len(user) == 0: #array doesn't exist
        flash("Invalid email")
        return redirect ('/')
    else:
        if bcrypt.check_password_hash(user[0]['password'], password):
            flash ("Logged in!")
            session['first_name'] = (user[0]['first_name'])
            return redirect ('/profile')
        else:
            flash ("Invalid password")
            return redirect ('/')


@app.route('/profile')
def profile():
    return render_template('profile.html', first_name = session['first_name'])


@app.route('/logout')
def logout():
    session.pop('first_name')
    session.pop('_flashes', None)
    return redirect ('/')

app.run(debug=True)

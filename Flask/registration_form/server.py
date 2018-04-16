from flask import Flask, render_template, request, redirect, session, flash
from datetime import datetime
import re #needed for re.compile below
app=Flask (__name__)
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    print "Got Post Info"
    now=datetime.now().strftime('%YYYY-%mm-%dd')
    errors=False
    if len(request.form['first_name'])<1:
        flash("First Name field cannot be empty")
        errors=True
    elif not request.form['first_name'].isalpha():
        flash("First Name can contain only letters")
        errors=True

    if len(request.form['last_name'])<1:
        flash("Last Name field cannot be empty")
        errors=True
    elif not request.form['last_name'].isalpha():
        flash("Last Name can contain only letters")
        errors=True

    if len(request.form['email'])<1:
        flash("Email field cannot be empty")
        errors=True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email not valid")
        errors=True

    if len(request.form['pw'])==0:
        flash("Password field cannot be empty")
        errors=True
    elif len(request.form['pw'])<8:
        flash("Password must be greater than 8 characters")
        errors=True
    elif not PASSWORD_REGEX.match(request.form['pw']):
        flash("Password must contain at least one capital and lowercase letter, and at least one number")
        errors=True

    if len(request.form['pwconfirm'])<1:
        flash("Password Confirmation field cannot be empty")
        errors=True
    elif request.form['pw'] != request.form['pwconfirm']:
        flash ("Passwords do not match")
        errors=True

    if len(request.form['bd'])<1:
        flash("Birthday field cannot be empty")
        errors=True

    if not errors:
        flash("Success!")

    return redirect('/')

app.run(debug=True)

from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key="secret"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    print email
    if len(email)<1:
        flash("Email field cannot be empty")
        print "Nothing entered"
        return redirect ('/')
    if not EMAIL_REGEX.match(email):
        flash("Email is not valid")
        print "Email fail"
        return redirect('/')
    else:
        query = "INSERT INTO email(email, created_at) VALUES (:email, NOW())"
        data = {
            'email': request.form['email'] #from form, value is name='email'
        }
        session['email'] = email #enter value into session in order to display in '/success'
        mysql.query_db(query, data) #function defined in mysqlconnection.py, parameters needed
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails, email=session['email'])

@app.route('/remove_email/<email_id>')
def remove(email_id):
    query = "DELETE FROM email WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)

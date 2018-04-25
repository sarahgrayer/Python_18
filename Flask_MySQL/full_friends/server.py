from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends_db')
app.secret_key="secret"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/') #display off of the friends on the index.html page
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST']) #handle the 'add friend' form submit & create the friend in the db
def create():
    query = "INSERT INTO friends (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
            }
    mysql.query_db(query, data)
    print "friend added"
    return redirect('/')

@app.route('/friends/<friend_id>/edit') #display the edit friend page for the particular friend
def edit(friend_id):
    query = "SELECT id, first_name, last_name, email FROM friends WHERE id = :id"
    data = {
        'id':friend_id
        }
    friend = mysql.query_db(query, data)[0]
    mysql.query_db(query, data)
    print "editting"
    return render_template('edit.html', friend=friend)

@app.route('/friends/<friend_id>', methods=['POST']) #handle the 'edit friend' form submit & update the friend in the db
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
        "first_name": request.form['f_name'],
        "last_name": request.form['l_name'],
        "email": request.form['e_mail'],
        "id": (friend_id) #{{friend.id}} in .html substitues in the /friends/1 routing, then when posted to route, it's parsed out and passed as function (friend_id)
        }
    mysql.query_db(query, data)
    print "updated"
    return redirect('/')

@app.route('/friends/<friend_id>/delete') #delete friend from db
def destroy(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect ('/')

app.run(debug=True)

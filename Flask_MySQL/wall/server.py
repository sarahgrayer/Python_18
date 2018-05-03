from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt (app)
mysql = MySQLConnector(app,'wall')
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
            get_id = mysql.query_db("SELECT * from users WHERE email=:email", data)
            session['user'] = get_id[0]
            #session['first_name'] = (user[0]['first_name'])
            return redirect ('/wall')
        else:
            flash ("Invalid password")
            return redirect ('/')


@app.route('/wall', methods=['POST', 'GET'])
def profile():
    print "the wall"
    query = "SELECT users.id AS user_id, messages.id AS message_id, messages.message, messages.created_at, users.first_name, users.last_name FROM messages JOIN users ON users_id=users.id"
    messages = mysql.query_db(query) #messages is now name of dict, this query returns an array of key:val data which we will extract from
    query_comments = "SELECT comments.messages_id, comments.comment, comments.id, comments.created_at, comments.users_id FROM comments JOIN messages ON messages.id = comments.messages_id JOIN users ON comments.users_id"
    comments = mysql.query_db(query_comments)
    print messages
    return render_template('wall.html', user=session['user'], messages = messages, comments = comments)


@app.route('/post', methods=['POST'])
def post():
    message=request.form['message']
    if len(message)>0:
        #print session['id']
        query= "INSERT INTO messages (message, users_id, created_at) VALUES (:message, :user_id, NOW())"
        data = {
            'message': message,
            'user_id': session['id'],
        }
        mysql.query_db(query, data)
        flash ("You posted a message!")
        print "message posted"
    else:
        flash ("Please enter a post")
        return redirect('/wall')
    return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    print "processing comment"
    #message = mysql.query_db(query, data)[0]
    #mysql.query_db(query, data)
    if len(comment)>0:
        query = "INSERT INTO comments (comment, users_id, created_at, messages_id) VALUES (:comment, :users_id, NOW(), :messages_id)"
        data = {
            'comment': request.form['comment'],
            'users_id': session['id'],
            'messages_id': message_id,
            }
        mysql.query_db(query, data)
        flash("You posted a comment!")
        print "comment posted"
        return redirect('/wall')
    else:
        flash ("Please enter a post")
        return redirect('/wall')



@app.route('/logout')
def logout():
    session.pop('user_id')
    session.pop('_flashes', None)
    return redirect ('/')

app.run(debug=True)

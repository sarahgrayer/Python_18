from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='secret'#need secret key for security purposes w/sessions

#this route will handle rendering of our form
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


#this route will handle form submission, defined which HTTP methods are allowed by this route
@app.route('/users', methods=["POST"])
def create_user():
    print "Got Post Info" #this prints to terminal
    #name= request.form['name']
    #email= request.form['email']
    #store the name and email below using sessions, allows ability to use the info in other functions
    session['name']=request.form['name']
    session['email']=request.form['email']
    print "did we make it?"
    return redirect('/show')

@app.route('/show')
def show_user():
    print "Got Post data again"
    return render_template('user.html')

app.run(debug=True)

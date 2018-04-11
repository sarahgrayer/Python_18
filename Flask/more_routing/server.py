from flask import Flask, render_template, request, redirect
app=Flask (__name__)

#this route will handle rendering of our form
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


#this route will handle form submission, defined which HTTP methods are allowed by this route
@app.route('/users', methods=["POST"])
def create_user():
    print "Got Post Info" #this prints to terminal
    name= request.form['name']
    email= request.form['email']
    return redirect('/')

app.run(debug=True)

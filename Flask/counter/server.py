from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='secret'

#this route will increment the 'counter' by one w/each refresh
@app.route('/', methods=["GET"])
def index():
    try:
        session['counter']+= 1
    except:
        session['counter']=1
    return render_template("index.html")

#increments 'counter' by 2 (one here and one in ('/'))
@app.route('/add_two', methods=["POST"])
def add_two():
    session['counter']+= 1
    return redirect('/')

#resets 'counter' to 1
@app.route('/reset', methods=["POST"])
def reset():
    session['counter']= 0
    return redirect('/')

app.run(debug=True)

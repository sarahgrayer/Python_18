from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key='secret'

#plus a random integer in sessions with each refresh to ('/')
@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,101)
    return render_template("index.html")

#assigns value to session['result']
@app.route('/guess', methods=["POST"])
def guess():
    print 'guess route'
    print session['random_num'] #cheat
    if session['random_num'] == int(request.form['guess']):
        session['result'] = 'correct'
        print 'you got it!'
    elif session['random_num'] <int(request.form['guess']):
        session['result'] = 'high'
        print "too high"
    else:
        session['result'] = 'low'
        print 'too low'
    return redirect('/')

#if statements prevent from resetting multiple times. .pop would cause an error if nothing defined.
@app.route('/reset')
def reset():
    if 'random_num' in session:
        session.pop('random_num')
    if 'result' in session:
        session.pop('result')
    return redirect('/')

app.run(debug=True)

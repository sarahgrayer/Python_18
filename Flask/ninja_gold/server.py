from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app=Flask(__name__)
app.secret_key='secret'

#plus a random integer in sessions with each refresh to ('/')
@app.route('/')
def index():
    if 'gold_count' not in session:
        session['gold_count'] = 0
        session['activities'] = []
    return render_template("index.html", gold_count=session['gold_count'], activities=session['activities'])

@app.route('/process', methods=["POST"])
def process():
    now=datetime.now().strftime("%I:%M%p, %m/%d/%Y")
    location=request.form['location']
    print now
    act = {}
    act['time'] = now
    act['win'] = True

    if location=='farm':
        gold= random.randint(10,21)
        print gold
        act['location'] = 'farm'
        act['gold'] = gold

    elif location=='cave':
        gold = random.randint(5,11)
        print gold
        act['location'] = 'cave'
        act['gold'] = gold

    elif location=='house':
        gold= random.randint(2,6)
        print gold
        act['location'] = 'house'
        act['gold'] = gold

    else:
        gold= random.randint(-50,51)
        if gold > 0:
            print gold
            act['location'] = 'casino'
            act['gold'] = gold
        else:
            print gold
            act['location'] = 'casino'
            act['gold'] = abs(gold)
            act['win'] = False

    session['gold_count'] += gold
    session['activities'].append(act)
    return redirect('/')

#if statements prevent from resetting multiple times. .pop would cause an error if nothing defined.
@app.route('/reset')
def reset():
    if 'gold_count' in session:
        session.pop('gold_count')
    if 'activities' in session:
        session.pop('activities')
    return redirect('/')

app.run(debug=True)

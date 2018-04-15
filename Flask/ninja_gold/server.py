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
    now=datetime.now().strftime("%I:%M%p, %m/%d/%Y") #hour:minute pm, month/date/year
    location=request.form['location']
    print now
    act = {} #creates in an instance which we will append to session["activities"]
    act['time'] = now #variable now defined above w/datetime function, no '' needed
    act['win'] = True

    if location=='farm':
        gold= random.randint(10,21)
        print gold
        act['location'] = 'farm' # need '', referencing value of hidden input type
        act['gold'] = gold #variable gold defined above w/random function, no '' needed

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
            act['gold'] = abs(gold) #need abs value here, otherwise will print "lost -'gold' gold"
            act['win'] = False #defined True above until here

    session['gold_count'] += gold
    session['activities'].append(act)
    print (act) #[{'win': True, 'location': 'cave', 'gold': 7, 'time': '04:09PM, 04/15/2018'}]
    print session['activities'] #[{act}, {act}, {act}..]
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

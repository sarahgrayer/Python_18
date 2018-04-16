from flask import Flask, render_template, request, redirect, session, flash
import os, sys


app=Flask (__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def show():
    images = os.listdir(os.path.join(app.static_folder, "images"))
    return render_template("show_all.html", images = images)

@app.route('/ninja/<color>')
def show_ninja(color):
    ninjas = {
    'orange':'Michelangelo',
    'blue':'Leonardo',
    'red':'Raphael',
    'purple':'Donatello'
    }
    if color in ninjas:
        character = ninjas[color]
        print character
    else:
        character='Not April'
    return render_template("show.html", character=character)

app.run(debug=True)

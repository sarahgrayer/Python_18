from flask import Flask, render_template, request, redirect, session, flash
import os, sys


app=Flask (__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign_in')
def sign_in():
    return render_template("sign_in.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/profile', methods=["POST"])
def profile():
    return render_template("profile.html")

app.run(debug=True)

from flask import Flask, render_template, request, redirect
app=Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html")

#this route will handle form submission
@app.route('/process', methods=["POST"])
def create_user():
    print "Got Post Info"
    name= request.form['name']
    location= request.form['location'] #name=location in form, used in info.html
    language= request.form['language']
    return render_template("info.html", name=name, location=location, language=language)

app.run(debug=True)

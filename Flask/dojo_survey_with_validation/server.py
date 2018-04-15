from flask import Flask, render_template, request, redirect, session, flash

app=Flask (__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

#this route will handle form submission
@app.route('/process', methods=["POST"])
def process():
    print "Got Post Info"
    errors=False
    if len(request.form['name'])<1:
        flash("Name field cannot be empty")
        errors=True
    if len(request.form['comment'])<1:
        flash("Comment field cannot be empty")
        errors=True
    if len(request.form['name'])>120:
        flash("Comment field cannot be longer than 120 characters")
        errors=True

    if errors:
        return redirect('/')

    #use session to pass all form data to next route /info
    if not errors:
        session["submitted_info"] = request.form
        return redirect('/info')

@app.route('/info')
def info():
    return render_template("info.html", result=session["submitted_info"])

app.run(debug=True)

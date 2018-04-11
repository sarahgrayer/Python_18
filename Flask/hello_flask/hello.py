from flask import Flask #Improt Flask to allow us to create our "app" variable. Need this line in every application built in Flask
app = Flask(__name__) #Global variable __name__ tells flask whether we are running the file directly, or importing it as a module

@app.route('/') #The '@' symbol designates a "decorator", which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.

def hello_world():
    return "Hello World!" #return "Hello World!" to the response

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True) #run app in debug mode

#to open in browser, first open .py file in terminal, then navigate to localhost:5000

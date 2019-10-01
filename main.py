
from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def sign_up():
    username = request.form["username"]
    password_input = request.form["password"]
    verify_password_input = request.form["verify_password"]

    verify_password_error = ""

    if password_input != verify_password_input:
        verify_password_error = "Passwords do not match!"
        return render_template('index.html', username=username, verify_password_error=verify_password_error)

    else:
        return render_template('welcome.html', username=username)


app.run()
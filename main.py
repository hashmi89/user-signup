
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = file(templates/index.html)

@app.route("/")
def index():
    return form

app.run()
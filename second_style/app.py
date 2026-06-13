# basic flask app
from flask import Flask, render_template
from static.scripts.dataDict import projects as projects


app = Flask(__name__)

reload = True
@app.route('/')
def home():
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
    #config flask environment variable
    # export FLASK_APP=app.py
    # export FLASK_ENV=development
    # flask run
    
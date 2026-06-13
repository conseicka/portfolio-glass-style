# basic flask app
from flask import Flask, render_template


app = Flask(__name__)
reload = True
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    #config flask environment variable
    # export FLASK_APP=app.py
    # export FLASK_ENV=development
    # flask run
    
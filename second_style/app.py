# basic flask app
from flask import Flask, render_template
from static.scripts.dataDict import projects as projects
from static.scripts.dataDict import career as career


app = Flask(__name__)

reload = True
@app.route('/')
def home():
    return render_template('index.html', projects=projects, career=career)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

    
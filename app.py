# basic flask app
from flask import Flask, render_template
from static.scripts.dataDict import projects as projects
from static.scripts.dataDict import career as career


app = Flask(__name__)

reload = True
@app.route('/')
def home():
    return render_template('index.html', projects=projects, career=career)


@app.route('/project/<project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        return render_template('404.html'), 404
    return render_template('project-detail.html', project=project)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

    
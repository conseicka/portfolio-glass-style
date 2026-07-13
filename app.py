# basic flask app
from flask import Flask, render_template
from static.scripts.dataDict import projects as projects
from static.scripts.dataDict import career as career
from static.scripts.dataDict import jobbies as jobbies


app = Flask(__name__)

reload = True
@app.route('/')
def home():
    return render_template('index.html', projects=projects, career=career, jobbies=jobbies)


@app.route('/project/<project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        return render_template('404.html'), 404
    return render_template('project-detail.html', project=project)


@app.route('/job/<job_id>')
def job_detail(job_id):
    job = next((j for j in jobbies if j['id'] == job_id), None)
    if job is None:
        return render_template('404.html'), 404
    # normalize single-show jobs into assets list
    job_copy = dict(job)
    if ('assets' not in job_copy or not job_copy.get('assets')) and job_copy.get('show'):
        job_copy['assets'] = [{
            'name': job_copy.get('title', ''),
            'type': job_copy.get('type', 'image'),
            'show': job_copy.get('show'),
            'path': job_copy.get('show'),
            'description': job_copy.get('title', ''),
        }]
    return render_template('jobbies-details.html', job=job_copy)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

    
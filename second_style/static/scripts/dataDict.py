#make dict for html usage in project section based on projects.html




projects = [
    {
        "icon": "📁",
        "title": "My Portfolio v3",
        "description": "Futuristic developer portfolio with glassmorphism effects, neon lights, interactive visual components and pure HTML & CSS architecture.",
        "stack": ["HTML", "CSS", "UI Design"],
    },
    {
        "icon": "⚙️",
        "title": "Management System",
        "description": "Business management solution focused on database design, backend logic, and scalable architecture.",
        "stack": ["Java", "SQL", "Backend"],
    },
    {
        "icon": "🧪",
        "title": "Experimental Lab",
        "description": "Personal space for testing new ideas, technologies, visual concepts and software experiments.",
        "stack": ["Research", "Learning", "Innovation"],
    },
]

# Ejemplo de uso con Flask:
# from flask import render_template
# from projects_data import projects
#
# @app.route('/')
# def home():
#     return render_template('projects.html', projects=projects)

import os
from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

HOLA = os.getenv("HOLA")


def projectsPage(req):
    context = {'projects': projectsList}
    return render(req, 'pages/projects.html', context)


def projectPage(req, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    context = {'project': projectObj}
    return render(req, 'pages/single_Pro.html', context)

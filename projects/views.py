import os
from django.shortcuts import render

from projects.models import Project


HOLA = os.getenv("HOLA")


def projectsPage(req):
    projectsList = Project.objects.all()
    context = {'projects': projectsList}
    return render(req, 'pages/projects.html', context)


def projectPage(req, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {'project': projectObj, 'tags': tags}
    return render(req, 'pages/single_Pro.html', context)

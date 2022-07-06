import os
from django.shortcuts import render


HOLA = os.getenv("HOLA")


def projectsPage(req):
    return render(req, 'pages/projects.html')


def projectPage(req, pk):
    return render(req, 'pages/single_Pro.html')

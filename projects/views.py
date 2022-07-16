from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from projects.forms import ProjectForm

from projects.models import Project


def projectsPage(req):
    projectsList = Project.objects.all()
    context = {'projects': projectsList}
    return render(req, 'pages/projects.html', context)


def projectPage(req, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    context = {'project': projectObj}
    return render(req, 'pages/single_Pro.html', context)


@login_required(login_url='login')
def createProject(req):
    form = ProjectForm()

    if req.method == "POST":
        form = ProjectForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(req, 'pages/project_form.html', context)


def updateProject(req, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if req.method == "POST":
        form = ProjectForm(req.POST, req.FILES, instance=project,)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(req, 'pages/project_form.html', context)


def deleteProject(req, pk):
    project = Project.objects.get(id=pk)
    if req.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'obj': project}
    return render(req, 'pages/delete_object.html', context)

from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


def profilesPage(req):
    context = {}
    return render(req, 'pages/profiles.html', context)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'pages/login_register.html', context)


def logoutUser(req):
    logout(req)
    messages.info(request, 'User was logged out!')
    return redirect('login')

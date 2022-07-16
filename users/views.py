
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


def profilesPage(req):
    context = {}
    return render(req, 'pages/profiles.html', context)


def loginUser(request):
    page = 'login'
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

    context = {'page': page}
    return render(request, 'pages/login_register.html', context)


def logoutUser(req):
    logout(req)
    messages.info(req, 'User was logged out!')
    return redirect('login')


def registerUser(req):
    page = 'register'
    form = CustomUserCreationForm()

    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(req, 'User account was created!')
            login(req, user)
            return redirect('profiles')
        else:
            messages.error(req, 'An error has occurred during reg')
    context = {'page': page, 'form': form}
    return render(req, 'pages/login_register.html', context)

from django.shortcuts import redirect, render

# Create your views here.


def profilesPage(req):
    context = {}
    return render(req, 'pages/profiles.html', context)

from django.shortcuts import render

# Create your views here.


def attacksPage(req):
    context = {}
    return render(req, 'pages/attacks.html', context)

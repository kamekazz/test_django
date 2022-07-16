from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tel_attack.models import Attack


# Create your views here.

@login_required(login_url='login')
def attacksPage(req):
    attacksList = Attack.objects.all()
    context = {'attacks': attacksList}
    return render(req, 'pages/attacks.html', context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tel_attack.forms import TelephoneForm

from tel_attack.models import Attack, TelephoneNumber


# Create your views here.

@login_required(login_url='login')
def attacksPage(req):
    attacksList = Attack.objects.all()
    context = {'attacks': attacksList}
    return render(req, 'pages/attacks.html', context)


@login_required(login_url='login')
def addPNPage(req):
    form = TelephoneForm()
    if req.method == "POST":
        form = TelephoneForm(req.POST)
        if form.is_valid():
            form.save()
    telephonesList = TelephoneNumber.objects.all()
    context = {'telephones': telephonesList, 'form': form}
    return render(req, 'pages/addPN.html', context)

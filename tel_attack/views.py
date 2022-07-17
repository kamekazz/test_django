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
def attackMapPage(req, pk):
    attack = Attack.objects.get(id=pk)
    context = {'attack': attack}
    return render(req, 'pages/attack_map.html', context)


@login_required(login_url='login')
def updateAttackPage(req, pk):
    attack = Attack.objects.get(id=pk)
    context = {'attack': attack}
    return render(req, 'pages/attack.html', context)


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


def startAttack(req, pk):
    print(pk)
    return render(req, 'pages/addPN.html')

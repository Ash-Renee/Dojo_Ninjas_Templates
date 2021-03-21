from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def index(request):
    context = {"all_dojo": Dojo.objects.all(), "message": "UwU"}
    return render(request, 'index.html', context)

def people(request):
    Ninja.objects.create(
        first_name= request.POST['first_name'],
        last_name= request.POST['last_name'],
        dojos_id= request.POST['dojos_id'],
    )
    print(request.POST)
    return redirect("/")

def building(request):
    Dojo.objects.create(
        name= request.POST['name'],
        city= request.POST['city'],
        state= request.POST['state'],
    )
    print(request.POST)
    return redirect("/")
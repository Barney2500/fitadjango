from django.shortcuts import render
from .models import *

def index(request):
    automobils = Automobil.objects.all()
    return render(request, 'index.html', {'automobils': automobils})
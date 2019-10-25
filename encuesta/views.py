from django.shortcuts import render
from .models import *

def pag_ppal(request):
    return render(request, 'encuesta/pag_ppal.html',{})

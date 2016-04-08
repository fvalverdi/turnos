#from django.http import HttpResponse
from django.shortcuts import render
#from .models import Turnos

def pacientes_list(request):
        return render(request, 'turnos/pacientes_list.html', {})

# Create your views here.

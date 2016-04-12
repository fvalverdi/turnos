#from django.http import HttpResponse
from django.shortcuts import render
from .models import Turnos

def pacientes_list(request):

		posts = Turnos.objects.all()
        return render(request, 'turnos/pacientes_list.html', {'posts': posts})

# Create your views here.

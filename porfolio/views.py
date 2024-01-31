from django.shortcuts import render
from .models import Project


# Funcion de inicio de la web ; nos envia a cada apartado a un estilo linktree
def init_view(request):
    return render(request, 'init.html')

# Funcion que llama a los projectos dentro de home
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

# Funcion que llama a Morrospacehtml
def Morrospace(request):
    return render(request, 'Morrospace.html')

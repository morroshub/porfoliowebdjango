from django.shortcuts import render
from .models import Project


# Funcion de inicio de la web ; nos envia a cada apartado a un estilo linktree
def init_view(request):
    return render(request, 'init.html')

# Funcion que llama a los projectos dentro de home
def Projects(request):
    projects = Project.objects.all()
    return render(request, 'Projects.html', {'projects': projects})

# Funcion que llama a Morrospacehtml
def Morrospace(request):
    return render(request, 'Morrospace.html')


def your_view(request):
    context = {
        'facebook_url': 'https://www.facebook.com/your-facebook-page',
        'github_url': 'https://github.com/your-github-profile',
        'youtube_url': 'https://www.youtube.com/your-channel',
        'discord_url': 'https://discord.gg/your-discord-server',
        # Add more social media URLs as needed
    }

    return render(request, 'layout.html', context)

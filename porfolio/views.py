from .models import Project
from django.shortcuts import render
# from django.shortcuts import redirect para errores 3xx
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError # Manejo de errores 
from django_nextjs.render import render_nextjs_page_sync

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from porfolio.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



# def index(request):
#     return render_nextjs_page_sync(request, '/index')

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



def index(request):
    return render(request, "layout.html")


# Manejo de errores :

# # 3xx
# def custom_301(request):
#     return redirect('nueva_ruta', permanent=True)

# def custom_302_with_message(request):
#     context = {'mensaje': 'Esta página se ha movido temporalmente.'}
#     return render(request, '302_with_message.html', context, status=302)


# 4xx
def custom_403(request, exception=None):
    return render(request, '403.html', status=403)

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


# 5xx
def custom_500(request):
    return render(request, '500.html', status=500)


def social_views(request):
    context = {
        'facebook_url': 'https://www.facebook.com/your-facebook-page',
        'github_url': 'https://github.com/your-github-profile',
        'youtube_url': 'https://www.youtube.com/your-channel',
        'discord_url': 'https://discord.gg/your-discord-server',
        # Add more social media URLs as needed
    }

    return render(request, 'layout.html', context)

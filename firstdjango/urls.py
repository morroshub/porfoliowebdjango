from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from porfolio.views import Projects, init_view, Morrospace

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', init_view, name='Init'),
    path('Projects/', Projects, name='Projects'),
    path('Morrospace/', Morrospace, name='Morrospace'),
    path('blog/',include('blog.urls')), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
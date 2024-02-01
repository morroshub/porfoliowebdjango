from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from porfolio.views import Projects, init_view, Morrospace, index

urlpatterns = [
    
    path("reactpy/", include("reactpy_django.http.urls")),
    path('admin/', admin.site.urls),
    path('', init_view, name='Init'),
    path('Projects/', Projects, name='Projects'),
    path('Morrospace/', Morrospace, name='Morrospace'),
    path('blog/',include('blog.urls')), 
    path("example/", index, name='Index'),
    path('',include('porfolio.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
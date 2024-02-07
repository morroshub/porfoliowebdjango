from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from porfolio.views import Projects, init_view, Morrospace, index



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('blog/', include('blog.urls')),
    path('porfolio/', include('porfolio.urls')),
    path("", include("django_nextjs.urls")),
    # path("", init_view, name="init_view"),
    # path('', include(router.urls)),
    # path('', init_view, name='Init'),
    # path('Morrospace/', Morrospace, name='Morrospace'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
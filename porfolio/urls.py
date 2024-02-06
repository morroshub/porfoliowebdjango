from django.urls import include, path
from rest_framework import routers

from porfolio import views
from .views import init_view

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

    path("", init_view, name="init_view"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
]

urlpatterns += router.urls



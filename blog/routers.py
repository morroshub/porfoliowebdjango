from rest_framework.routers import DefaultRouter
from blog import views


# API versioning
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet, basename='post')
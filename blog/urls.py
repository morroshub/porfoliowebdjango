from django.urls import path, include
from .routers import router
from blog.views import *
from rest_framework.documentation import include_docs_urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'blog'

urlpatterns = [
    
    path('docs', include_docs_urls(title="blogAPI")),
    path('api/v1/', include(router.urls)),
    path("blog/", render_posts, name='posts'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<int:post_id>/', post_detail, name='post_detail')
]

urlpatterns += router.urls
 
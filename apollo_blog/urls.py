
from django.contrib import admin
from django.urls import path, include
from apollo_blog.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('blog.urls'), name='about'),
    path('', index, name='index'),
]

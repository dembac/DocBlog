from django.urls import path
from .views import index


urlpatterns = [
    path('dem', index, name="blog-index" ),


]
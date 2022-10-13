from django.urls import path

from . import views


urlpatterns = [
    # path('', views.create, name='create'),
    path('', views.read_all, name='read all'),
    path('<int:index>', views.read, name='read'),
]
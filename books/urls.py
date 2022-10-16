from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='create'),
    path('<int:index>', views.one, name='read'),
]

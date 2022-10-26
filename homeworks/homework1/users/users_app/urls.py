from django.urls import path

from . import views

urlpatterns = [  # URLConf
    path('', views.index),
    path('do_something', views.do_sth),
]
from django.urls import path

from . import views

urlpatterns = [
    path('appusers', views.AppUserList.as_view()),
    path('appusers/<int:pk>', views.AppUserDetail.as_view()),

]

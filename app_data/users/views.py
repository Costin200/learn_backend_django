from django.shortcuts import render

# Create your views here.


from users.models import AppUser


# functie care parcurgea toti utilizatorii aplicatiei
def show_all():
    appusers = AppUser.objects.all()
    for user in appusers:
        print(user)

from rest_framework.request import HttpRequest


def welcome(request):
    show_all()
    return HttpRequest()

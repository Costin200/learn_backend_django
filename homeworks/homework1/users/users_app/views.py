from django.http import HttpResponse


def index(request):
    return HttpResponse('success')


def do_sth(request):
    return HttpResponse('done something')
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

#
# CRUD   Create Read Update Delete

books = [
    "To Kill a Mockingbird", "Lord of The Rings"
]

# Create
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def create(request):
    print(request.body)
    return JsonResponse(request.body, content_type='application/json', safe=False)


# Read

def read_all(request):
    return JsonResponse(json.dumps({"books": books}), content_type='application/json', safe=False)


def read(request, index):
    return JsonResponse(json.dumps({"book": books[index]}), content_type='application/json', safe=False)

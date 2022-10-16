import json

import django.http.response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#
# CRUD   Create Read Update Delete

books = [
    "To Kill a Mockingbird",
    "Lord of The Rings"
]

# Pentru request-ul care foloseste metoda POST, este nevoie sa descriem cum
#  arata formularul:

from django import forms


# Urmatorul form corespunde cu un dictionar  {"book": "un string"}
class BookForm(forms.Form):
    book = forms.CharField(max_length=100)


@csrf_exempt
def index(request):
    if request.method == 'POST':
        """
            What is parsing?
            when the request from insomnia contains a form (multipart),
            request.body will look like this:
        
                b'--X-INSOMNIA-BOUNDARY
                Content-Disposition: form-data; name="book"
                
                Learn And Grow Rich
                --X-INSOMNIA-BOUNDARY
                Content-Disposition: form-data; name="genre"
                
                Motivation
                --X-INSOMNIA-BOUNDARY--
                '
            
            Parser translate encoded data, such as the form above,
            into data we can use.
            
            E.g. By running 
                
            form = BookForm(request.POST)
            print(form.data)
            
            form.data will contain:
            
            <QueryDict: {'book': ['Learn And Grow Rich'], 'genre': ['Motivation']}>
            
            * form.files will contain the files
            
            
        """
        print(request.body)

        # parse the form from the request
        form = BookForm(request.POST)

        book = form.data.get('book')
        books.append(book)

        return JsonResponse({"books": books}, content_type='application/json')
    elif request.method == 'GET':
        return JsonResponse({"books": books})


@csrf_exempt
def one(request, index: int):
    # Treat the errors:
    if index >= len(books) or index < 0:
        return HttpResponse(f"Book Of Index={index} Not Found", status=404)
    if request.method == 'POST':
        return HttpResponse('POST method not permitted', status=405)

    if request.method == 'GET':
        return JsonResponse({"book": books[index]})

    if request.method == 'DELETE':
        del books[index]
        return JsonResponse({"books": books})

    # TODO for replacing and updating books, there are more methods (PUT, PATCH)
    #      but for using them we'll need to use Django REST Framework

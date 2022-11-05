# REST API Basics

The essential operations for a server is storing and updating data.

We can do these operations using a Database Management System (abbr. DBMS), such as MySQL, Postgres, Oracle etc.

* But can we tell our users to use even the GUI of a DBMS? No, we can't.

This is why the applications they use (Smartphone apps, websites, desktop programs installed on Windows/MacOS) need
a simple way of communicating with the database.

(Moreover, more complex operations such as querying users with a certain characteristics, fetching and ordering the data
of only some users etc. are even more complex to execute using a DBMS or any SQL flavor).

## Long story short..

API = Application Programming Interface

They are tools we implement so that the end user's devices can interact with the Database easily.

Thank to their existence, many useful features can be easily implemented and scaled:

* Sharing the same data to multiple users easily and instantly
* Syncing data across multiple devices
* You write/update the API once and it can be integrated/updated across all devices (smartphones, PCs, watches etc)

## 1. The Models/Entities

Each time you create an Django Application using

```shell
python manage.py startapp APP_NAME
```

you get a file named `APP_NAME/models.py`.

Inside `models.py` you can write your models. Each model represents a unique Entity/Table from the database.

E.g. If you have an application which enables people to play live chess, you probably add entities such as `Player`
, `Match`, `MatchHistory`

### How to implement?

_using classes:_

```python
# library
from django.db import models    

# database entity
class AppUser(models.Model):    
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    email = models.EmailField()
```

`django.db.models`, imported simply as `models`, is a library included in Django, already imported inside `APP_NAME/models.py` 
and contains many data types used for you Entity's table:
* CharField
* IntegerField
* EmailField
* DateTimeField
* ImageField

## 2. The Endpoints/Routes (named views in Django)

In DRF (Django Rest Framework), before creating the APIView we need serializer classes.

What does "serialize" means? It means transforming/transposing data to and from two different representations.

E.g. When you create an object in Python it is represented like this:
```python
from django.db import models
class Car(models.Model):
    nake = models.CharField(max_length=100)

if __name__ == '__main__':
    car = Car(make="Model 3")
    print(car)
```

but to store it into a file we may need the JSON representation:

```python
{
    "make": "Model 3"
}
```

What serializers basically do is permit the transformation of Models into their JSON shape. Why do we need JSON data? Because it 
can be used universally by frontend libraries, android implementations, IOS implementations and desktop applications.


```python



class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
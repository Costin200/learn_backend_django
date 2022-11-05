from rest_framework.decorators import permission_classes

from books.models import Book

from books.models import Book
from books.serializers import BookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


@permission_classes((permissions.AllowAny,))
class BookList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Book.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class BookDetail(APIView):
    """
    Retrieve, update or delete a Book instance.
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Book = self.get_object(pk)
        serializer = BookSerializer(Book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Book = self.get_object(pk)
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Book = self.get_object(pk)
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

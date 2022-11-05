from django.shortcuts import render
from rest_framework.decorators import permission_classes

# Create your views here.


from users.models import AppUser

from users.models import AppUser
from users.serializers import AppUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


@permission_classes((permissions.AllowAny,))
class AppUserList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = AppUser.objects.all()
        serializer = AppUserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class AppUserDetail(APIView):
    """
    Retrieve, update or delete a AppUser instance.
    """
    def get_object(self, pk):
        try:
            return AppUser.objects.get(pk=pk)
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        AppUser = self.get_object(pk)
        serializer = AppUserSerializer(AppUser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        AppUser = self.get_object(pk)
        serializer = AppUserSerializer(AppUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        AppUser = self.get_object(pk)
        AppUser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
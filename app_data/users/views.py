from django.shortcuts import render

# Create your views here.


from users.models import AppUser

from users.models import AppUser
from users.serializers import AppUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from rest_framework.decorators import permission_classes


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

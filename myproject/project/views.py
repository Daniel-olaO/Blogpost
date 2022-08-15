from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def start(request):
    content = {"message":"API listening"}
    return Response(content, status=status.HTTP_200_OK)
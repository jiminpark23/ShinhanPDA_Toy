from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .serializers import MemberSerializer # serializer 가져오기

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView   
):
    serializer_class = MemberSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
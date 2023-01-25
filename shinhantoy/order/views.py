from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from .models import Order
from .serializers import OrderSerializer

# Create your views here.

class OrderListView(
    mixins.ListModeMixins,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        
        # queryset
        # serialize
        # return response
        
        return self.list(request, args, kwargs)
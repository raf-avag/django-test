from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = ProductSerializer(products, many=True)
        return Response({"products": data.data})

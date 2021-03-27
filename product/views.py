from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json
from django.contrib.auth.models import User
from .models import Product
from django.urls import reverse
from user.models import Profile
from django.http import JsonResponse

from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )

from .serializers import ProductListSerializer, ProductDetailSerializer
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.

class ProductListView(ListAPIView):
	serializer_class = ProductListSerializer
	queryset = Product.objects.all()
	def get(self, request, *args, **kwargs):
		queryset = Product.objects.all()
		queryset = sorted(queryset, reverse=True, key=lambda product: product.total_upvotes)
		serializer = ProductListSerializer(queryset, many=True)
		return Response(serializer.data)

class ProductCreateView(CreateAPIView):
	serializer_class = ProductDetailSerializer
	queryset = Product.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	serializer_class = ProductDetailSerializer
	queryset = Product.objects.all()

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class Upvote(APIView):
	def post(self, request, *args, **kwargs):
		product = get_object_or_404(Product, pk=kwargs['pk'])
		user = request.user
		if user in product.upvote.all():
			product.upvote.remove(user.id)
		else:
			product.upvote.add(user.id)
		context = {'upvoters': product.upvoters}
		return Response (context)

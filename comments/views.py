from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Comment
from django.urls import reverse
from user.models import Profile
from django.http import JsonResponse, HttpResponseRedirect


from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
    )

from .serializers import CommentSerializer, CommentDetailSerializer

# Create your views here.

class CommentListView(ListAPIView):
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

# class ProductCreateView(CreateAPIView):
# 	serializer_class = ProductDetailSerializer
# 	queryset = Product.objects.all()

# 	def perform_create(self, serializer):
# 		serializer.save(user=self.request.user)


class CommentDetailView(RetrieveAPIView):
	serializer_class = CommentDetailSerializer
	queryset = Comment.objects.all()

	# def perform_update(self, serializer):
	# 	serializer.save(user=self.request.user)
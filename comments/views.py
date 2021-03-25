from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Comment, ReplyComment
from django.urls import reverse
from user.models import Profile
from product.models import Product
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

from .serializers import CommentSerializer, ReplyCommentCreateSerializer, CommentCreateSerializer

# Create your views here.

class CommentListView(ListAPIView):
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

class CommentCreateView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.request.query_params['pk'])
        serializer.save(user=self.request.user, product=product)

class ReplyCreateView(CreateAPIView):
    serializer_class = ReplyCommentCreateSerializer
    queryset = ReplyComment.objects.all()

    def perform_create(self, serializer):
        comment = get_object_or_404(Comment, pk=self.request.query_params['pk'])
        serializer.save(user=self.request.user, comment=comment)


# class CommentDetailView(RetrieveAPIView):
# 	serializer_class = CommentDetailSerializer
# 	queryset = Comment.objects.all()

	# def perform_update(self, serializer):
	# 	serializer.save(user=self.request.user)
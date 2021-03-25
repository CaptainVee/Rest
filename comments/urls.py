from django.contrib import admin
from django.urls import path

from .views import CommentCreateView, ReplyCreateView


urlpatterns = [
    # path('', CommentListView.as_view(), name='list'),
    path('create/', CommentCreateView.as_view(), name='create-comment'),
    path('reply/create/', ReplyCreateView.as_view(), name='create-reply'),
    # path('upvote/<int:pk>', Upvote.as_view(), name='upvote'),
]

from django.contrib import admin
from django.urls import path

from .views import CommentListView, CommentDetailView


urlpatterns = [
    path('', CommentListView.as_view(), name='list'),
    # path('comment/create/', ProductCreateView.as_view(), name='create-product'),
    path('<int:pk>/detail', CommentDetailView.as_view(), name='comment-detail'),
    # path('upvote/<int:pk>', Upvote.as_view(), name='upvote'),
]

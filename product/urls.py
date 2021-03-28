from django.contrib import admin
from django.urls import path

from .views import ProductListView, ProductCreateView, ProductRetrieveUpdateDestroyView, Upvote
from .views import CommentCreateView, ReplyCreateView


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/<int:pk>/detail/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('upvote/<int:pk>/', Upvote.as_view(), name='upvote'),
    path('comment/create/', CommentCreateView.as_view(), name='create-comment'),
    path('comment/reply/create/', ReplyCreateView.as_view(), name='create-reply'),
]

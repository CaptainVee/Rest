from django.contrib import admin
from django.urls import path

from .views import ProductListView, ProductCreateView, ProductRetrieveUpdateDestroyView, Upvote


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/<int:pk>/detail', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('upvote/<int:pk>', Upvote.as_view(), name='upvote'),
]

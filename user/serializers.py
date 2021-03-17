from rest_framework.serializers import ModelSerializer, SerializerMethodField

from django.contrib.auth.models import User
from user.models import Profile
from product.models import Product
from product.serializers import ProductListSerializer

from rest_framework import serializers


class UserDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	email = SerializerMethodField()
	product = SerializerMethodField()

	class Meta:		
		model = Profile
		fields = ('user', 'picture', 'email', 'product')

	def get_user(self, obj):
		return (obj.user.username)

	def get_email(self, obj):
		return (obj.user.email)

	def get_product(self, obj):
		product_queryset = Product.objects.filter(author=obj.id)
		product = ProductListSerializer(product_queryset, many=True).data
		return product



			
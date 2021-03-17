from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from .models import Product, TAGS
from django.contrib.auth.models import User
from rest_framework import fields, serializers

class ProductListSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = (
			'url',
			'name',
			'topics',
			'caption',
			'thumbnail',
			'total_upvotes',
			'id',
			)

class ProductDetailSerializer(ModelSerializer):
	topics = fields.MultipleChoiceField(TAGS)
	class Meta:
		model = Product
		fields = (
			'url',
			'name',
			'topics',
			'caption',
			'upvote',
			'thumbnail',
			'download_link',
			'status',
			'twitter_url',
			'content',
			'launch_date',
			'created_at',
			)


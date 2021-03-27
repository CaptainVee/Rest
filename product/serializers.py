from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from .models import Product, TAGS
from django.contrib.auth.models import User
from rest_framework import fields, serializers
from comments.models import Comment
from comments.serializers import CommentSerializer
class ProductListSerializer(ModelSerializer):
	comments = SerializerMethodField()
	class Meta:
		model = Product
		fields = (
			'url',
			'name',
			'topics',
			'comments',
			'caption',
			'thumbnail',
			'total_upvotes',
			'upvoters',
			'id',
                        'launch_date',
			)

	def get_comments(self, obj):
		''' this function gets the total replies and comments 
			then add them up to give the overall comments
			 '''
		total = []

		queryset = Comment.objects.filter(product=obj.id)
		comments = CommentSerializer(queryset, many=True).data
		for comment in comments:
			total.append(comment['total_replies'])

		total_replies = sum(total)
		total_comments = queryset.count()
		overall_comment = total_comments + total_replies

		return overall_comment



class ProductDetailSerializer(ModelSerializer):
	topics = fields.MultipleChoiceField(TAGS)
	comments = SerializerMethodField()
	total_comments = SerializerMethodField()
	username = SerializerMethodField()
	user = SerializerMethodField()
	user_profile = HyperlinkedIdentityField(view_name='profile', lookup_field='pk')
	class Meta:
		model = Product
		fields = (
			'id',
			'username',
			'user',
			'user_profile',
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
			'total_comments',
			'comments',
			)

	def get_comments(self, obj):
		queryset = Comment.objects.filter(product=obj.id)
		comments = CommentSerializer(queryset, many=True).data
		return comments

	def get_user(self, obj):
		return (obj.user.id)

	def get_username(self, obj):
		return (obj.user.username)


	def get_total_comments(self, obj):
		''' this function gets the total replies and comments 
			then add them up to give the overall comments
			 '''
		total = []

		queryset = Comment.objects.filter(product=obj.id)
		comments = CommentSerializer(queryset, many=True).data
		for comment in comments:
			total.append(comment['total_replies'])

		total_replies = sum(total)
		total_comments = queryset.count()
		overall_comment = total_comments + total_replies

		return overall_comment









from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from .models import Comment, ReplyComment
from rest_framework import fields, serializers

class CommentSerializer(ModelSerializer):
	replies = SerializerMethodField()
	username = SerializerMethodField()
	total_replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = (
			'id',
			'username',
			'content',
			'timestamp',
			'total_replies',
			'replies',
			)

	def get_replies(self, obj):
		queryset = ReplyComment.objects.filter(comment=obj.id)
		replies = ReplyCommentSerializer(queryset, many=True).data
		return replies

	def get_total_replies(self, obj):
		queryset = ReplyComment.objects.filter(comment=obj.id)
		return queryset.count()

	def get_username(self, obj):
		return (obj.user.username)

class CommentCreateSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields =(
			'content',
			)

class ReplyCommentSerializer(ModelSerializer):
	username = SerializerMethodField()
	class Meta:
		model = ReplyComment
		fields = (
			'timestamp',
			'content',
			'username',
			)

	def get_username(self, obj):
		return (obj.user.username)

class ReplyCommentCreateSerializer(ModelSerializer):
	class Meta:
		model = ReplyComment
		fields = (
			'content',
			)






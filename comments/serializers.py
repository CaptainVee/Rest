from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from .models import Comment, ReplyComment
from rest_framework import fields, serializers

class CommentSerializer(ModelSerializer):
	replies = SerializerMethodField()
	total_replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = (
			'user',
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



class ReplyCommentSerializer(ModelSerializer):
	class Meta:
		model = ReplyComment
		fields = (
			'timestamp',
			'content',
			)


class CommentDetailSerializer(ModelSerializer):
	reply_count = SerializerMethodField()
	replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = (
			'content_type',
			'object_id',
			'content',
			'id',
			'replies'
			)

	def get_replies(self, obj):
		if obj.is_parent:
			return CommentChildSerializer(obj.children(), many=True).data
		return None

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0












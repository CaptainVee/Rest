from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from .models import Comment
from rest_framework import fields, serializers

class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = (
			'content_type',
			'object_id',
			'parent',
			'content',
			'id',
			)
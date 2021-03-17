from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	parent = models.ForeignKey('self', null=True, blank=True)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)


	class Mete:
		ordering = ['-timestamp']
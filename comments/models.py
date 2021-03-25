from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from product.models import Product


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content

class ReplyComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']








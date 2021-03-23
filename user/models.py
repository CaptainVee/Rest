from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


from product.models import Product
# Create your models here.


class Profile(models.Model):
	picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
	about = models.CharField(max_length=150)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.id


	@property
	def product(self):
		return self.product_set.all().order_by('-created_at')


class Chat(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)

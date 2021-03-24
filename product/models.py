from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from user.models import Profile
from django.db.models.signals import post_save
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.contrib.contenttypes.models import ContentType
# Create your models here.

TAGS = (
    (1, 'IT and Software'),
    (2, 'Design'),
    (3, 'Personal Development'),
    (4, 'Marketing'),
    (5, 'Music'),
    (6, 'Cloud')
)

STATUS = (
    ('S', 'Private'),
    ('P', 'Public'),
    ('I', 'In_progress')
)

from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer 
class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id',
			)

class Product(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	caption = models.CharField(max_length=200)
	download_link = models.CharField(max_length=150, blank=True)
	status = models.CharField(choices=STATUS, max_length=1)
	topics = MultiSelectField(choices=TAGS, max_length=6)
	content = models.TextField()
	launch_date = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)
	twitter_url = models.CharField(max_length=100, blank=True)
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	thumbnail = models.ImageField(default='default.jpg', null=True, blank=True)
	upvote = models.ManyToManyField(User, blank=True, related_name='posts')

	def __str__(self):
		return self.name

	@property	
	def total_upvotes(self):
		return self.upvote.count()

	@property	
	def upvoters(self):
		queryset = self.upvote.all()
		voters = UserSerializer(queryset, many=True).data
		return voters


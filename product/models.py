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
from django.core.validators import MaxValueValidator, MinValueValidator
import statistics
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
	# upvotes = models.IntegerField(blank=True, null=True, default=1)
	upvote = models.ManyToManyField(User, blank=True, related_name='posts')

	def __str__(self):
		return self.name

	@property	
	def total_upvotes(self):
		return self.upvote.count()


# class Reviews(models.Model):
# 	'''this model is for reviews about the course'''
# 	created_at = models.DateTimeField(default=timezone.now)
# 	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
# 	updated_at = models.DateTimeField(default=timezone.now)
# 	product = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	body = models.TextField()
# 	star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True)
# 	# likes = models.ManyToManyField(User, blank=True, )

# 	def __str__(self):
# 		return self.created_by.username


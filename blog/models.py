from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE) ## if a user is deleted then so is the post

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})


class Contractor(models.Model):
	full_name = models.CharField(max_length = 35, default = '')
	industry = models.CharField(max_length = 20, default = '')
	bio = models.TextField(default = '', blank = True)


class Listing(models.Model):
	company = models.ForeignKey(USer, on_delete = models.CASCADE)
	listing = models.ManyToManyField('Contractor', related_name='listings')
	date_posted = models.DateTimeField(default = timezone.now)
	date_updated = models.DateTimeField(auto_now = True)



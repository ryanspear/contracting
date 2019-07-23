from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	## String describing this instace of profile
	def __str__(self):
		return f'{self.user.username} Profile'

	# Resize the image if it is bigger than the greatest size we show.
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300: ## if larger than our largest size we display
			output_size = (300,300) 
			img.thumbnail(output_size)
			img.save(self.image.path) # save over previous image

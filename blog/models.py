from django.db import models
from django.utils import timezone

# Create your models here.
# Always start a class name with an uppercase letter (django dudes taught me that)
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Skill(models.Model):
	listText = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)

	def publish(self):
		self.save()
		
	def __str__(self):
		return self.listText
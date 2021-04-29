from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
	title = models.CharField(max_length=500, null=False, blank=False)
	post = models.TextField(max_length=5000, null=False, blank=False)

	def __str__(self):
		return f"{self.title}"

	def get_absolute_url(self):
		return reverse('details', args=[str(self.id)])

	class Meta:

		ordering = ['-date_created']

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

	def __str__(self):

		return f"{self.post.title} - {self.user}"



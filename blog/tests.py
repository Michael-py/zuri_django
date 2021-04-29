from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class PostTestCase(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='testuser',
			email='test@email.com',
			password='secret'
			)

		self.post = Post.objects.create(
			title='God Bless Nigeria',
			post='This Naija sef',
			author=self.user,
			)

	def test_string_representation(self):
		post = Post(title='A sample title')
		self.assertEqual(str(post), post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'God Bless Nigeria')
		self.assertEqual(f'{self.post.author}', 'testuser')
		self.assertEqual(f'{self.post.post}', 'This Naija sef')

	def test_post_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'This Naija sef')
		self.assertTemplateUsed(response, 'blog/home.html')

	def test_post_detail_view(self):
		response = self.client.get('/article/1/')
		no_response = self.client.get('/articles/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'God Bless Nigeria')
		self.assertTemplateUsed(response, 'blog/details.html')

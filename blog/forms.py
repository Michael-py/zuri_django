from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):

	class Meta:
		model = Post

		fields = [
			'author',
			'title',
			'post',
		]

class CommentForm(forms.ModelForm):
	content = forms.CharField(label ="", widget = forms.Textarea(
		attrs ={
		'class':'form-control',
		'placeholder':'Comment here !',
		'rows':4,
		'cols':50
		}))

	class Meta:
		model = Comment
		fields =['content']
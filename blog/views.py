from django.shortcuts import (render, 
								redirect, 
								get_object_or_404, 
								HttpResponseRedirect,
								HttpResponse)
from django.contrib import messages
from .models import *
# from django.contrib.auth.models import User
from .forms import RegisterForm, PostForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
 
# Create your views here.

def index(request):

	return render(request, 'blog/index.html')

def home(request):
	posts = Post.objects.all()
	count = posts.count()

	context = {
	'posts': posts,
	'count':count,}

	return render(request, 'blog/home.html', context)

def details(request, post_id):
	post = Post.objects.get(id=post_id)
	comments = post.comments.all().order_by('-date_created')

	if request.method == 'POST':
		cf = CommentForm(request.POST or None)

		if cf.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(post =post, user=request.user, content = content)

			comment.post = post

			comment.save()

			return redirect(post.get_absolute_url())

	else:

		cf = CommentForm()

	context ={

	'post':post,
	'comment_form':cf,
	'comments': comments,
	# 'comment': comment,

      }

	return render(request, 'blog/details.html', context)

def add_new(request):

	form = PostForm(request.POST or None)

	if form.is_valid():
		form.save()

		messages.success(request, 'You have successfully created an article.')

		return redirect('home')

	return render(request, 'blog/add_new.html', {'form':form})

def update(request, post_id):

	obj = get_object_or_404(Post, id=post_id)
	objs = Post.objects.all()

	form = PostForm(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return redirect("/article/"+ post_id)

	return render(request, "blog/update.html", {'form':form})


def delete(request, post_id):

	obj = get_object_or_404(Post, id=post_id)

	if request.method =="POST":
		obj.delete()

		return HttpResponseRedirect("/home/")

	return render(request, "blog/delete.html", {})


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/login/")

		else:
			messages.error(response, 'Ensure password is 8 characters long.')
			
	else:
		form = RegisterForm()

	return render(response, "registration/register.html", {"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")
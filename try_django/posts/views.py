from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully created a post")
		return redirect('/posts/')
	else:
		messages.error(request, "Posting ERROR. Try again!")
	context = {
		"form": form
	}
	return render(request, 'posts/post_form.html', context)


def post_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance": instance,
	}
	return render(request, 'posts/post_detail.html', context)


def posts_home(request):
	posts_content = Post.objects.all()
	total_post_count = len(posts_content)
	paginator = Paginator(posts_content, 5)
	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"content": posts_content,
		"total": total_post_count,
	}
	return render(request, 'posts/posts_home.html', context)


def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully edited a post")
		return redirect("/posts/")

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, 'posts/post_form.html', context)


def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect("/posts/")


def home_page(request):
	context = {
		"title": "Home",
	}
	return render(request, 'base.html', context)

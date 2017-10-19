from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import PostAdd_form
from .  import models

# Create your views here.

def home(request):
	posts = models.posts.objects.all().order_by('published_on')
	context = {'posts': posts}
	return(render(request,'blog.html', context))


def posts(request, post_id):
	post = models.posts.objects.get(id=post_id)
	img = str(post.image)
	context = {'post': post, 'image': img[7:]}
	return(render(request,'post.html', context))


def add(request):
	if(request.method == 'POST'):
		form = PostAdd_form(request.POST)
		if(form.is_valid()):
			post = form.save(commit = False)
			post.posted_by = request.user
			post.published_on = timezone.now()
			post.save()
			return(HttpResponseRedirect('/'))
		else:
			context = {'errors': form.errors}
			return(render(request, 'add.html', context))
	else:
		return(render(request,"add.html", {}))


def contact(request):
	return(render(request,'contact.html', {}))


def about(request):
	return(render(request,'about.html', {}))

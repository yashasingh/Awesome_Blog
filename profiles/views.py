from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import signup_form
# Create your views here.


def login(request):
    if(request.user.is_authenticated()):
        return(HttpResponseRedirect('/'))
    elif(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,
                                 password = password)
        if user and user.is_active:
            auth.login(request,user)
            return(HttpResponseRedirect('/'))
        else:
            context = {'errors': 'invalid attempt'}
            return(render(request, 'login.html', context))
    else:
        return(render(request, 'login.html', {}))


def logout(request):
    if(request.user.is_authenticated()):
        auth.logout(request)
    return(HttpResponseRedirect('/'))


def signup(request):
    if(request.method == 'POST'):
        form = signup_form(request.POST)
        if(form.is_valid()):
            user = form.save(commit = False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return(HttpResponseRedirect('/'))
        else:
            context = {'errors': form.errors}
            return(render(request,'signup.html'), context)
    else:
        return(render(request,'signup.html', {}))

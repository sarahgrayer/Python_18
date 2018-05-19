from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from . import models
from models import User
from django.contrib.messages import error
from django.contrib import messages

def index(request):
    return render(request, 'users/index.html')

def register(request):
    #process Registration, add to db, redirect to  /success
    result = User.objects.validate_register(request.POST)
    print "back from validating registration"
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
        messages.success(request, "Successfully registered!")
        return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    print "back from validating login"
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'users/success.html', context)

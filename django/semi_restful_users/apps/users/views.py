# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from . import models
from models import User
from django.contrib.messages import error

# Create your views here.
def index(request): #context retrieves all info on file for User objects
    context = {
        "users":User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    #display form to add new user
    return render(request, 'users/create.html')

def create(request):
    #insert new user into db. POST sent from users/new. redirect to ('/').
    errors = User.objects.validate(request.POST) #validate function in models
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/new')

    User.objects.create( #creates new User object
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
    )
    return redirect('/')

def show(request, user_id):
    #display info for particular user passed in
    context = {
        'user': User.objects.get(id=user_id) #grab info from user table for this id
    }
    return render(request, 'users/show.html', context)

def edit(request, user_id):
    #display form to edit user id
    context = {
        'user': User.objects.get(id=user_id) #grab info from user table for this id
    }
    return render(request, 'users/edit.html', context)

def update(request, user_id):
    #process form sent from /edit. Redirect to users/show.
    errors = User.objects.validate(request.POST) #validate function in models
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/{}/edit'.format(user_id))

    this_user = User.objects.get(id=user_id)
    this_user.first_name = request.POST['first_name']
    this_user.last_name = request.POST['last_name']
    this_user.email = request.POST['email']
    this_user.save()
    print this_user
    return redirect('/users')

def destroy(request, user_id):
    #remove particular user w/given id. redirect back to ('/')
    User.objects.get(id=user_id).delete()
    return redirect('/users')

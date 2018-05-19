# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.

urlpatterns = [
    url(r'^$', views.index), #render login/reg page
    url(r'^register$', views.register), #validate, add to db, redirect to ('/')
    url(r'^login$', views.login), #validate, redirect to welcome page
    url(r'^welcome/(?P<user_id>\d+)$', views.welcome), #render welcome page, user_id passed in
    url(r'^create$', views.create), #render add book page
    url(r'^review$', views.review), #validates, adds review to db, redirects to book
    url(r'^book/(?P<book_id>\d+)/show$', views.book), #render book page passed in
    url(r'^user/(?P<user_id>\d+)/show$', views.user), #renders user page, passed in
]

def index(request): #render login/reg page
    return render (request, "books/index.html")

def welcome(request, user_id): #render welcome page, user_id passed in
    context = {
        'user':User.objects.get(id=user_id)
    }
    return render (request, "books/welcome.html", context)

def create(request): #render add book page
    return render (request, "books/create.html")

def book(request, book_id): #render book page passed in
    context = {
        'book':Book.objects.get(id=book_id)
    }
    return render (request, "books/index.html", context)

def user(request, user_id): #renders user page, passed in
    context = {
        'user':User.objects.get(id=user_id)
    }
    return render (request, "books/show_user.html", context)

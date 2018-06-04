# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.core import serializers

def index(request):
    return render (request, "notes/index.html")

def create(request):
    Note.objects.create(content=request.POST['content'])
    notes=Note.objects.all()
    return render(request, "notes/show.html", {"notes": notes})

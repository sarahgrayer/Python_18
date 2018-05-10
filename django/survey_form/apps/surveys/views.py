# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    try:
        request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['attempt'] += 1
    return redirect ('/result')

def result(request):
    return render(request, 'surveys/success.html')

def back(request):
    del request.session['name']
    del request.session['location']
    del request.session['language']
    del request.session['comment']
    return redirect('/')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    try:
        request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0
    return render(request, 'random_word/index.html')

def create(request):
    request.session['attempt'] += 1
    request.session['word'] = get_random_string(14)
    print request.session['attempt']
    return redirect ('/')

def reset(request):
    del request.session['attempt']
    del request.session['word']
    return redirect('/')

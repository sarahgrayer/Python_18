# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    try: #when there is something stored in session['attempt'], just return render
        request.session['attempt']
    except KeyError: #ker error is returned when there is nothing stored in session, so start w/0
        request.session['attempt'] = 0
    return render(request, 'random_word/index.html')

def create(request):
    request.session['attempt'] += 1 #increment attempt #
    request.session['word'] = get_random_string(14) #generate random string w/14 characters
    print request.session['attempt']
    return redirect ('/')

def reset(request):
    del request.session['attempt'] #remove value from session['attempt']
    del request.session['word']
    return redirect('/')

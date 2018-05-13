# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'session/index.html')

def process(request):
    if "the_list" not in request.session:
        request.session['the_list'] = []
    else:
        request.session['the_list'] = request.session['the_list']
    if 'font_size' in request.POST:
        big = True
    else:
        big = False
    print "process 2"
    new_word_dict = {
        "word": request.POST['word'],
        "color": request.POST['color'],
        "big": big,
        "time": datetime.now().strftime("%H:%M %p, %B %d")
    }
    print "process 3"
    request.session['the_list'].append(new_word_dict)
    print "process 4", new_word_dict
    print request.session['the_list']
    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

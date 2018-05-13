# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import random
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    return render(request, "ninja/index.html")

def process(request):
    time = datetime.now().strftime("%I:%M%p, %m/%d/%Y")
    new_gold = 0
    action = "earned"
    location = request.POST['location']

    if location == 'farm':
        new_gold = random.randrange(10,21)
    elif location == 'cave':
        new_gold = random.randrange(5,11)
    elif location == 'house':
        new_gold = random.randrange(2,6)
    else:
        new_gold = random.randrange(-50, 50)
        if new_gold < 0:
            action = 'lost'

    new_activity = {
        'class': action, #defined above, 'earned' unless 'lost' at casino. Class determines color of message in index.html, with <li class = "{{i.class}}">{{i.message}}</li>
        'message': "You {} {} golds from the {} - {}".format(action, abs(new_gold), location, time)
    }
    try:
        log_list = request.session['logs'] #each new_activity gets appended to this list to loop through in index page as ul. Initiate with try/except. 
    except KeyError:
        log_list = []

    request.session['total'] += new_gold
    log_list.append(new_activity)
    request.session['logs'] = log_list
    return redirect('/')

def reset(request):
    del request.session['total']
    del request.session['logs']
    return redirect('/')

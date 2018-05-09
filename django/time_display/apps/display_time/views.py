# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
    "date":strftime("%b %d, %Y", gmtime()),
    "time":strftime("%I:%M:%S %p")
    }
    return render(request, 'display_time/index.html', context)

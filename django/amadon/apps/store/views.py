# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products import items #product.py file
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if "last_transaction" in request.session.keys(): #clear session to not duplicate charges on refresh
        del request.session['last_transaction']
    context = { #items defined in products.py file, referenced at top
        "items": items
    }
    return render(request, 'store/index.html', context)

def process(request, item_id):
    for item in items:
        if item['id'] == int(item_id): #match item bought to item_id in products
            amount_charged = item['price'] * int(request.POST['quantity'])
    #handle exceptions for keys if they do not exist yet
    if 'total_charged' not in request.session:
        request.session['total_charged'] = 0
    if 'total_items' not in request.session:
        request.session['total_items'] = 0

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect ('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')

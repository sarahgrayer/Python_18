# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
    def validate_register(self, post_data):
        errors = []
        #name
        if len(post_data['first_name'])<3 or len(post_data['last_name'])<3:
            errors.append("Please enter Name's with at least 3 characters.")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append("Please enter Name's with only letters")
        #email
        #if not re.match(EMAIL_REGEX, post_data['email']):
        if not EMAIL_REGEX.match(post_data['email']):
            errors.append("Invalid email")
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("Email already in use")
        #pw
        if len(post_data['password'])<8:
            errors.append("Please enter a Password with at least 8 characters.")
        if post_data['confirm_pw'] != post_data['password']:
            errors.append("Passwords do not match.")
        if not errors:
            hashed = bcrypt.hashpw((post_data['password']).encode(), bcrypt.gensalt(5))
            new_user = self.create(
                first_name = post_data['first_name'],
                last_name = post_data['last_name'],
                email = post_data['email'],
                password = hashed
            )
            return new_user
        print "done w/validating registration"
        return errors

    def validate_login(self, post_data):
        errors=[]
        #check db for thie email
        if len(self.filter(email=post_data['email']))>0:
            #check db for pw
            user=self.filter(email=post_data['email'])[0] #set user to the db entry that matches
            if not bcrypt.checkpw((post_data['password']).encode(), user.password.encode()): #parameter is what was entered, parameter 2 is what was stored in user.password. True means they match.
                errors.append('password incorrect')
        else: #if no email matching in db (line 14)
            errors.append('email and/or  password is incorrect')

        if errors:
            return errors
        else:
            print "login validated"
        return user

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    def __str__(self):
        return self.email

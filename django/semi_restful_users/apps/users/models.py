# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        #check for blank fields
        for field, value in post_data.iteritems():
            if len(value)<1:
                errors[field] = "{} field is required".format(field.replace('_', ''))
        #check for valid Email
        if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "Invalid email"
        #if emial is valid, check db for existing Email
        else:
            if len(self.filter(email=post_data['email']))>1:
                errors['email'] = "Email already in use"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()
    def __str__(self):
        return self.email

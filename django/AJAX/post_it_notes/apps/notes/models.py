# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class NoteManager(models.Manager):
    def validate_note(self, post_data):
        errors = []
        if len(post_data['content'])<1:
            errors.append("Please enter a note")
        if not errors:
            return self.create(
                content = post_data['content'],
            )
        return errors

class Note(models.Model):
    content = models.TextField()

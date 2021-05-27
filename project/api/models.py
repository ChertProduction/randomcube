from django.db import models

class Results(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    name = models.CharField(max_length=30)

from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
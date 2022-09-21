from pickle import TRUE
from sqlite3 import Date
from django.db import models
import os
from django.db.models.deletion import CASCADE
import django.utils.timezone
from django.contrib.auth.models import AbstractUser

class register1(AbstractUser):
    personal_option = [
        ('Faculty Member', 'Faculty Member'),
        ('UITC Staff', 'UITC Staff'),
        ('Student', 'Student'),
    ]
    Personal_description = models.CharField(max_length = 40, null=False, choices= personal_option)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')



class index(models.Model):
    User_name = models.CharField(max_length= 50, null=False)
    Password_data =models.CharField(default= "", max_length =40, null=False, unique = True)


    
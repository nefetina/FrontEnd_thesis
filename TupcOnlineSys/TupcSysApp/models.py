from multiprocessing.sharedctypes import Value
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
    idno = models.CharField(max_length= 20, null=False)
    Status = models.CharField(max_length=50, default = "On process" , null=False)


class index(models.Model):
    User_name = models.CharField(max_length= 50, null=False)
    Password_data =models.CharField(default= "", max_length =40, null=False, unique = True)


#faculty
class faculty_ID(models.Model):
    ff_name = models.CharField(max_length= 50, null=False)
    fm_name = models.CharField(max_length= 50, null=False)
    fl_name = models.CharField(max_length= 50, null=False)
    f_suffix = models.CharField(max_length= 50, null=True)
    f_emp = models.CharField(max_length = 100, null=False)
    f_datereq = models.DateField()
    f_daterel = models.DateField()
    f_gsis = models.CharField(max_length = 100, null=True)
    f_gsisp = models.CharField(max_length = 100, null=True)
    f_tin = models.CharField(max_length = 100, null=True)
    f_pagibig = models.CharField(max_length = 100, null=True)
    f_phil = models.CharField(max_length = 100, null=True)
    f_other = models.CharField(max_length = 100, null=True)
    f_cp = models.CharField(max_length = 100, null=True)
    f_num = models.CharField(max_length = 100, null=True)
    f_add = models.CharField(max_length = 200, null=True)
    f_signature = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    





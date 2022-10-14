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

class pics(models.Model):
    Usernamep= models.CharField(max_length= 50, null=False)
    pic = models.FileField(max_length=254)


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
    
#faculty wifi request
class faculty_wifi(models.Model):
    gf_name = models.CharField(max_length= 100, null=False)
    g_dept = models.CharField(max_length = 100, null=True)
    g_des = models.CharField(max_length = 100, null=True)
    g_sys = models.CharField(max_length = 100, null=True)
    g_mac = models.CharField(max_length = 100, null=True)
    g_num = models.CharField(max_length = 100, null=True)
    g_email = models.CharField(max_length = 100, null=True)
    g_fac = models.CharField(max_length = 100, null=True)
    g_sig = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    g_datereq = models.DateField()
    g_stats = models.CharField(max_length = 100, null=True)

#student wifi record
class student_wifi(models.Model):
    gf_name1 = models.CharField(max_length= 100, null=False)
    g_csec1 = models.CharField(max_length = 100, null=True)
    g_snum1 = models.CharField(max_length = 100, null=True)
    g_sem1 = models.CharField(max_length = 100, null=True)
    g_or1 = models.CharField(max_length = 100, null=True)
    g_sys1 = models.CharField(max_length = 100, null=True)
    g_mac1 = models.CharField(max_length = 100, null=True)
    g_num1 = models.CharField(max_length = 100, null=True)
    g_email1 = models.CharField(max_length = 100, null=True)
    g_add1 = models.CharField(max_length = 100, null=True)
    g_sig1 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    g_daterec1 = models.DateField()
    g_stats1 = models.CharField(max_length = 100, null=True)

#student internet access record
class student_internet(models.Model):
    gf_name2 = models.CharField(max_length= 100, null=False)
    g_csec2 = models.CharField(max_length = 100, null=True)
    g_snum2 = models.CharField(max_length = 100, null=True)
    g_sem2 = models.CharField(max_length = 100, null=True)
    g_or2 = models.CharField(max_length = 100, null=True)
    g_num2 = models.CharField(max_length = 100, null=True)
    g_email2 = models.CharField(max_length = 100, null=True)
    g_add2 = models.CharField(max_length = 100, null=True)
    gu_name2 = models.CharField(max_length = 100, null=True)
    g_sig2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    g_daterec2 = models.DateField()
    g_stats2 = models.CharField(max_length = 100, null=True)

#schedules record
class sched_rec(models.Model):
    hf_name = models.CharField(max_length= 100, null=False)
    h_dept = models.CharField(max_length = 100, null=True)
    h_daterec = models.DateField()
    hl_num = models.CharField(max_length = 100, null=True)
    h_csec = models.CharField(max_length = 100, null=True)
    hs_time = models.TimeField()
    he_time = models.TimeField()
    h_sig = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    h_stats = models.CharField(max_length = 100, null=True)

#repair and maintenance record
class repmain_rec(models.Model):
    i_type = models.CharField(max_length= 100, null=False)
    i_brand = models.CharField(max_length = 100, null=True)
    is_num = models.DateField()
    i_spec = models.CharField(max_length = 100, null=True)
    i_notbd = models.CharField(max_length = 100, null=True)
    if_name = models.CharField(max_length = 100, null=True)
    i_pos = models.CharField(max_length = 100, null=True)
    i_dept = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_sig = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_daterec = models.DateField()
    i_time = models.TimeField()
    ii_assess = models.CharField(max_length = 100, null=True)
    i_assessby = models.CharField(max_length = 100, null=True)
    i_sig = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_dateass = models.DateField()
    ip_assign = models.CharField(max_length = 100, null=True)
    i_quant = models.CharField(max_length = 100, null=True)
    i_units = models.CharField(max_length = 100, null=True)
    i_partics = models.CharField(max_length = 100, null=True)
    i_avail = models.CharField(max_length = 100, null=True)
    i_approve = models.CharField(max_length = 100, null=True)
    i_note = models.CharField(max_length = 100, null=True)
    i_coords = models.CharField(max_length = 100, null=True)
    i_sig1 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_daterec1 = models.DateField()
    i_time1 = models.TimeField()
    iu_pers = models.CharField(max_length = 100, null=True)
    i_sig2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    is_date = models.DateField()
    is_time = models.TimeField()
    is_rec = models.CharField(max_length = 200, null=True)
    i_aor = models.CharField(max_length = 200, null=True)
    ie_user = models.CharField(max_length = 200, null=True)
    i_daterec2 = models.DateField()
    i_sig3 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_time2 = models.TimeField()
    i_stats = models.CharField(max_length = 100, null=True)

#maintenance record
class maintain_record(models.Model):
    i_type4 = models.CharField(max_length = 100, null=True)
    is_num4 = models.CharField(max_length = 100, null=True)
    i_datem = models.DateField()
    i_brand4 = models.CharField(max_length = 100, null=True)
    i_code = models.CharField(max_length = 100, null=True)
    ie_name = models.CharField(max_length = 100, null=True)
    iup_sstats = models.CharField(max_length = 100, null=True)
    i_remarks = models.CharField(max_length = 100, null=True)
    i_cobfs = models.CharField(max_length = 100, null=True)
    i_remarks2 = models.CharField(max_length = 100, null=True)
    iup_sstats2 = models.CharField(max_length = 100, null=True)
    i_remarks3 = models.CharField(max_length = 100, null=True)
    i_scan = models.CharField(max_length = 100, null=True)
    i_remarks4 = models.CharField(max_length = 100, null=True)
    ia_virus = models.CharField(max_length = 100, null=True)
    i_remarks5 = models.CharField(max_length = 100, null=True)
    im_stats = models.CharField(max_length = 100, null=True)
    i_remarks6 = models.CharField(max_length = 100, null=True)
    ik_stats = models.CharField(max_length = 100, null=True)
    i_remarks7 = models.CharField(max_length = 100, null=True)
    i_dust = models.CharField(max_length = 100, null=True)
    i_remarks8= models.CharField(max_length = 100, null=True)
    i_organize = models.CharField(max_length = 100, null=True)
    i_remarks9 = models.CharField(max_length = 100, null=True)
    i_wipe = models.CharField(max_length = 100, null=True)
    i_remarks10 = models.CharField(max_length = 100, null=True)
    i_run= models.CharField(max_length = 100, null=True)
    i_remarks11 = models.CharField(max_length = 100, null=True)
    i_defragement = models.CharField(max_length = 100, null=True)
    i_remarks12 = models.CharField(max_length = 100, null=True)
    i_empty = models.CharField(max_length = 100, null=True)
    i_remarks13 = models.CharField(max_length = 100, null=True)
    i_create = models.CharField(max_length = 100, null=True)
    i_remarks14 = models.CharField(max_length = 100, null=True)
    iu_pers4 = models.CharField(max_length = 100, null=True)
    i_sig4 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    is_date4 = models.DateField()
    is_time4 = models.TimeField()
    ie_date4 = models.DateField()
    ie_time4 = models.TimeField()
    is_rec4 = models.CharField(max_length = 200, null=True)
    ie_user4 = models.CharField(max_length = 200, null=True)
    i_sig4 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    ie_date5 = models.DateField()
    i_time2 = models.TimeField()
    i_stats = models.CharField(max_length = 100, null=True)

#borrowrecord
class borrow_record(models.Model):
    if_name5 = models.CharField(max_length = 100, null=True)
    i_date5 = models.DateField()
    i_time5 = models.TimeField()
    ir_borrow5 =  models.CharField(max_length = 100, null=True)
    irf_borrow5 =  models.CharField(max_length = 100, null=True)
    i_sig5 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_stats5 = models.CharField(max_length = 100, null=True)

#password reset student
class PassReset(models.Model):
    accounts = [
        ('GSFE', 'GSFE'),
        ('TUP EMAIL', 'TUP EMAIL'),
        ('MS TEAMS', 'MS TEAMS'),
        ('ERS ACCOUNT', 'ERS ACCOUNT'),
        ('NAS', 'NAS'),
    ]
    
    email = models.CharField(max_length = 100, null=True)
    emp_idno = models.CharField(max_length = 50, null=True)
    Account = models.CharField(max_length = 100, null=False, choices= accounts)
    

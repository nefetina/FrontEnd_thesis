from email.policy import default
from enum import unique
from multiprocessing.sharedctypes import Value
from pickle import TRUE
from sqlite3 import Date
from django.db import models
import os
from django.db.models.deletion import CASCADE
import django.utils.timezone
from django.contrib.auth.models import AbstractUser

class list(models.Model):
    lgsfe = models.CharField(max_length= 100, null=False)
    lidno = models.CharField(max_length= 50, null=False)
    type = models.CharField(max_length= 100, null=False)

class register1(AbstractUser):

    Personal_description = models.CharField(max_length = 40, null=True, default = "")
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    gsfe = models.CharField(max_length= 100, null=False)
    name = models.CharField(max_length= 100, null=False)
    #idno = models.ForeignKey(list, on_delete=models.CASCADE)
    #def __str__(self):
        #return self.idno
    

'''class UITC_borrow_record(models.Model):
    if_name5 = models.CharField(max_length = 100, null=True)
    i_date5 = models.DateField()
    i_time5 = models.TimeField()
    ir_borrow5 =  models.CharField(max_length = 100, null=True)
    irf_borrow5 =  models.CharField(max_length = 100, null=True)
    i_sig5 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    i_stats5 = models.CharField(max_length = 100, null=True)'''

#faculty #1L #f
class faculty_ID(models.Model):
    f_pic = models.TextField(max_length = 10000, null=True)
    email1 = models.CharField(max_length= 50, null=True)
    ff_name = models.CharField(max_length= 50, null=False)
    fm_name = models.CharField(max_length= 50, null=True)
    fl_name = models.CharField(max_length= 50, null=False)
    f_suffix = models.CharField(max_length= 50, null=True)
    f_emp = models.CharField(max_length = 100, null=False)
    f_datereq = models.DateField(null=True)
    f_daterel = models.DateField(null=True)
    f_gsis = models.CharField(max_length = 100, null=True)
    f_gsisp = models.CharField(max_length = 100, null=True)
    f_tin = models.CharField(max_length = 100, null=True)
    f_pagibig = models.CharField(max_length = 100, null=True)
    f_phil = models.CharField(max_length = 100, null=True)
    f_other = models.CharField(max_length = 100, null=True)
    f_cp = models.CharField(max_length = 100, null=True)
    f_num = models.CharField(max_length = 100, null=True)
    f_add = models.CharField(max_length = 200, null=True)
    f_signature = models.TextField(max_length = 10000, null=True)
    f_stat = models.CharField(max_length = 200, null=True)
    
#faculty wifi request #1M #g
class faculty_wifi(models.Model):
    gf_name = models.CharField(max_length= 100, null=False)
    g_dept = models.CharField(max_length = 100, null=True)
    g_des = models.CharField(max_length = 100, null=True)
    g_sys = models.CharField(max_length = 100, null=True)
    g_mac = models.CharField(max_length = 100, null=True)
    g_num = models.CharField(max_length = 100, null=True)
    g_email = models.CharField(max_length = 100, null=True)
    g_fac = models.CharField(max_length = 100, null=True)
    g_sig =models.TextField(max_length = 10000, null=True)
    g_datereq = models.DateField()
    g_stat = models.CharField(max_length = 100, null=True)

class faculty_lab(models.Model):
    email2 = models.CharField(max_length= 50, null=True)
    f_name = models.CharField(max_length= 100, null=False)
    dep = models.CharField(max_length = 100, null=True)
    l_date = models.DateField()
    lab_num = models.CharField(max_length = 100, null=True)
    crs_sec = models.CharField(max_length = 100, null=True)
    s_time = models.TimeField()
    e_time = models.TimeField()
    fl_sig = models.TextField(max_length = 10000, null=True)
    l_stat = models.CharField(max_length = 100, null=True)


class faculty_reports(models.Model):
    email3 = models.CharField(max_length= 50, null=True)
    ftype = models.CharField(max_length= 100, null=False)
    fbrand = models.CharField(max_length = 100, null=True)
    fserial = models.CharField(max_length= 100, null=False)
    fspecs = models.CharField(max_length = 100, null=True)
    fnature = models.CharField(max_length = 100, null=True)
    fname = models.CharField(max_length= 100, null=False)
    Fposjob = models.CharField(max_length= 100, null=False)
    fdep = models.CharField(max_length = 100, null=True)
    fdate = models.DateField()
    ftime = models.TimeField()
    fsign = models.TextField(max_length = 10000, null=True)
    fstat = models.CharField(max_length = 100, null=True)
    i_assessby = models.CharField(max_length = 100, null=True) #1E #i
    i_sig = models.TextField(max_length = 10000, null=True)
    i_dateass = models.DateField(null=True)
    ip_assign = models.CharField(max_length = 100, null=True)
    i_quant = models.CharField(max_length = 100, null=True)#
    i_units = models.CharField(max_length = 100, null=True)#
    i_partics = models.CharField(max_length = 100, null=True)#
    i_avail = models.CharField(max_length = 100, null=True)#
    i_approve = models.CharField(max_length = 100, null=True)#
    i_note = models.CharField(max_length = 100, null=True)#textarea1
    i_coords = models.CharField(max_length = 100, null=True)
    i_sig1 = models.TextField(max_length = 10000, null=True)
    i_daterec1 = models.DateField(null=True)
    i_time1 = models.TimeField(null=True)
    iu_pers = models.CharField(max_length = 100, null=True)
    i_sig2 = models.TextField(max_length = 10000, null=True)
    is_date = models.DateField(null=True)
    is_time = models.TimeField(null=True)
    ie_date = models.DateField(null=True) #walasadb
    ie_time = models.TimeField(null=True) #walasadb
    is_rec = models.CharField(max_length = 200, null=True) #textarea1
    i_aor = models.CharField(max_length = 200, null=True) #
    ie_user = models.CharField(max_length = 200, null=True)
    i_daterec2 = models.DateField(null=True)
    i_sig3 = models.TextField(max_length = 10000, null=True)
    i_time2 = models.TimeField(null=True)
    i_serv = models.CharField(max_length = 200, null=True)

class faculty_passreset(models.Model):
    id_type = [
        ('GSFE', 'GSFE'),
        ('TUP EMAIL', 'TUP EMAIL'),
        ('MS TEAMS', 'MS TEAMS'),
        ('ERS ACCOUNT', 'ERS ACCOUNT'),
        ('NAS', 'NAS'),
    ]
    fwname = models.CharField(max_length= 100, null=False)
    fwempID = models.CharField(max_length = 100, null=True)
    fwIDtype = models.CharField(max_length = 40, null=False, choices= id_type)
    fwemail = models.CharField(max_length = 100, null=True)
    fwstat = models.CharField(max_length = 100, null=True)

class faculty_borrow(models.Model):
    email4 = models.CharField(max_length= 50, null=True)
    fbname = models.CharField(max_length= 100, null=False)
    fbdate = models.DateField()
    fbtime = models.TimeField()
    fbreq = models.CharField(max_length= 100, null=False)
    fbreason = models.CharField(max_length = 100, null=True)
    fbsign = models.TextField(max_length = 10000, null=True)
    fbstat = models.CharField(max_length = 100, null=True)

#student wifi record #1Q #g
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
    g_sig1 = models.TextField(max_length = 10000, null=True)
    g_daterec1 = models.DateField()
    g_stats1 = models.CharField(max_length = 100, null=True)

#student internet access record #1Q #g
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
    g_sig2 = models.TextField(max_length = 10000, null=True)
    g_daterec2 = models.DateField()
    g_stats2 = models.CharField(max_length = 100, null=True)

#schedules record #1N #h
class sched_rec(models.Model):
    hf_name = models.CharField(max_length= 100, null=False)
    h_dept = models.CharField(max_length = 100, null=True)
    h_daterec = models.DateField()
    hl_num = models.CharField(max_length = 100, null=True)
    h_csec = models.CharField(max_length = 100, null=True)
    hs_time = models.TimeField()
    he_time = models.TimeField()
    h_sig = models.TextField(max_length = 10000, null=True)
    h_stats = models.CharField(max_length = 100, null=True)



    

#maintenance record #1E #i
class maintain_record(models.Model):
    i_type4 = models.CharField(max_length = 100, null=True)
    is_num4 = models.CharField(max_length = 100, null=True)
    i_datem = models.DateField()
    i_brand4 = models.CharField(max_length = 100, null=True)
    i_code = models.CharField(max_length = 100, null=True)
    ie_name = models.CharField(max_length = 100, null=True)
    iup_sstats = models.CharField(max_length = 100, null=True) #list1
    i_remarks = models.CharField(max_length = 100, null=True)
    i_cobfs = models.CharField(max_length = 100, null=True) #list1
    i_remarks2 = models.CharField(max_length = 100, null=True)
    iup_sstats2 = models.CharField(max_length = 100, null=True) #list1
    i_remarks3 = models.CharField(max_length = 100, null=True)
    i_scan = models.CharField(max_length = 100, null=True) #list1
    i_remarks4 = models.CharField(max_length = 100, null=True)
    ia_virus = models.CharField(max_length = 100, null=True) #list1
    i_remarks5 = models.CharField(max_length = 100, null=True)
    im_stats = models.CharField(max_length = 100, null=True) #list1
    i_remarks6 = models.CharField(max_length = 100, null=True)
    ik_stats = models.CharField(max_length = 100, null=True) #list1
    i_remarks7 = models.CharField(max_length = 100, null=True)
    i_dust = models.CharField(max_length = 100, null=True)#list1
    i_remarks8= models.CharField(max_length = 100, null=True)
    i_organize = models.CharField(max_length = 100, null=True)#list1
    i_remarks9 = models.CharField(max_length = 100, null=True)
    i_wipe = models.CharField(max_length = 100, null=True)#list1
    i_remarks10 = models.CharField(max_length = 100, null=True)
    i_run= models.CharField(max_length = 100, null=True)#list1
    i_remarks11 = models.CharField(max_length = 100, null=True)
    i_defragement = models.CharField(max_length = 100, null=True)#list1
    i_remarks12 = models.CharField(max_length = 100, null=True)
    i_empty = models.CharField(max_length = 100, null=True)#list1
    i_remarks13 = models.CharField(max_length = 100, null=True)
    i_create = models.CharField(max_length = 100, null=True)#list1
    i_remarks14 = models.CharField(max_length = 100, null=True)
    iu_pers4 = models.CharField(max_length = 100, null=True)
    is_date4 = models.DateField()
    is_time4 = models.TimeField()
    ie_date4 = models.DateField()
    ie_time4 = models.TimeField()
    is_rec4 = models.CharField(max_length = 200, null=True) #textarea1
    ie_user4 = models.CharField(max_length = 200, null=True)
    i_sig5 = models.TextField(max_length = 10000, null=True)
    ie_date5 = models.DateField()
    i_time2 = models.TimeField()
    i_stats = models.CharField(max_length = 100, null=True)
    i_sign = models.CharField(max_length = 100, null=True)


#borrowrecord #1O #i #r
class borrow_record(models.Model):
    email5 = models.CharField(max_length= 50, null=True)
    if_name5 = models.CharField(max_length = 100, null=True)
    i_date5 = models.DateField()
    i_time5 = models.TimeField()
    ir_borrow5 =  models.CharField(max_length = 100, null=True)
    irf_borrow5 =  models.CharField(max_length = 100, null=True)
    i_sig5 = models.TextField(max_length = 10000, null=True)
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
    psname = models.CharField(max_length = 100, null=True)
    email = models.CharField(max_length = 100, null=True)
    emp_idno = models.CharField(max_length = 50, null=True)
    Account = models.CharField(max_length = 100, null=True, choices= accounts)
    psstats = models.CharField(max_length = 100, null=True)

class Inventory(models.Model):
    i_quantity =  models.CharField(max_length = 100, null=True)
    i_equip =  models.CharField(max_length = 100, null=True)
    i_model =  models.CharField(max_length = 100, null=True)
    i_serial =  models.CharField(max_length = 100, null=True)


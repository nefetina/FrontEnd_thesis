import logging
from audioop import reverse
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import context
from operator import indexOf
from os import fstat
from unittest import loader
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage, message, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from MySQLdb import ROWID
from pip import List

from .forms import *
from .forms import Registration
from .models import *

# Create your views here.

installed_apps = ['TupcSysApp']

if str(register1.objects.all().values()) == "<QuerySet []>":
    print(register1.objects.all().values())
    admin = register1.objects.create_user(username="TUPC-00-0000", gsfe="tupc.uitconlinesystem@gmail.com", name="Admin", password="UITCtoken0001#", Personal_description="UITC Staff")
    admin.save()

"""def Document_save(request):
    if request.method=="POST":
        image = request.FILES["image"]
        idno = request.POST.get('idno')
        image_file = pics.objects.create(
                                       
                                       pic=image, idno=idno
                                      )
        image_path= image_file.pic.path




        image_path.save()
        return render(request, 'TupcSysApp/REGISTRATION.html', {"image_path":image_path})
    return render(request,  'TupcSysApp/REGISTRATION.html')"""
def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return redirect('/UitcPermission', data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return redirect('/UitcPermission')
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return redirect('/UitcPermission')

		file_data = csv_file.read().decode("utf-8")		

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:						
			fields = line.split(",")
			data_dict = {}
			data_dict["lgsfe"] = fields[0]
			data_dict["lidno"] = fields[1]
			data_dict["type"] = fields[2]
			try:
				form = form_list(data_dict)
				if form.is_valid():
					form.save()					
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass

	except Exception as e:
            pass
            return redirect('/UitcPermission')

def register(request):#registration
    form = Registration()
    if request.method == "POST":
        a = list.objects.all().values()
        b = request.POST.get("username")   
        c = request.POST.get("gsfe")
        ccc = list.objects.only('id').filter(lidno = b)
        y = ccc.values()         
        for x in y:
            print(x['type'])
            type = x['type']
            lgsfe = x['lgsfe']
            ids = x['id']
            
            
            if x["lidno"] == b and x['lgsfe'] == c:
                form =  Registration(request.POST)
                #form["Personal_description"].value = c
                if form.is_valid():
                    form.save()
                    register1.objects.filter(username=b).update(Personal_description=type)
                    messages.success(request, 'You are now successfully registered')
                    name = form["name"].value()
                    message = "You are succesfully registered as " + type + "! \n Your Username is " + b + '.'
                    email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [lgsfe],

                        )

                    email.send()

                    return redirect('/')
                else:
                    messages.warning(request, "Recheck all your input info")
            else:
                messages.warning(request, "Recheck all your input info")

                
    context = {
        'form':form
    }

    return render (request, 'TupcSysApp/REGISTRATION.html', context)
    
def index(request):#login page
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None and user.Personal_description == "UITC Staff":
            login(request, user)
            return redirect('/UitcHome')

        elif user is not None and user.Personal_description == "Faculty Member":
            login(request, user)
            return redirect('/FacultyHome')
        elif user is not None and user.Personal_description == "Student":
            login(request, user)
            return redirect('/StudentHome')
        else:
            messages.warning(request, 'Invalid Credentials')
    elif request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    
    return render (request, 'TupcSysApp/LOGIN.html')

@login_required(login_url='/Index')
def logoutUser(request):
    logout(request)
    request.user.Personal_description = None
    return redirect('/')


def facultyID_permit(request, id):
    a = faculty_ID.objects.get(id=id)
    current_user = request.user
    for x in faculty_ID.objects.only('id').filter(f_stat= "On process"):
        if a == x:
            x = faculty_ID.objects.filter(id=id).update(f_stat="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Evaluation of ID has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcID')

def facultyID_cancel(request, id):
    if request.method == 'POST':
        a = faculty_ID.objects.get(id=id)
        
        for x in faculty_ID.objects.only('id').filter(f_stat= "On process"):
            if a == x:
                x = faculty_ID.objects.filter(id=id).update(f_stat="Declined")
                y = faculty_ID.objects.filter(id=id).values()
                
                for x in y:
                    print(x['f_name'])
                    name = x['f_name']
                    asd = register1.objects.filter(name=name).values()
                    for z in asd:
                        uemail = z['gsfe']
                reason = request.POST.get("reason")
                print(name)
                print(reason)
                print(uemail)
                message = "Good day " + name + ", \n Your request for Laboratory Schedule has been declined, " + reason +"\n UITC admin"
                email = EmailMessage(
                            name,
                            message,
                            'tupc.uitconlinesystem@gmail.com',
                            [uemail],

                            )

                email.send()
                break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcID')

def FacultyWifi_cancel(request, id):
    a = faculty_wifi.objects.get(id=id)
    
    for x in faculty_wifi.objects.only('id').filter(g_stat= "On process"):
        if a == x:
            x = faculty_wifi.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcInternet')

def FacultyWifi_permit(request, id):
    a = faculty_wifi.objects.get(id=id)
    current_user = request.user
    for x in faculty_wifi.objects.only('id').filter(g_stat= "On process"):
        if a == x:
            x = faculty_wifi.objects.filter(id=id).update(g_stat="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Wifi Access has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcInternet')

def StudentWifi_cancel(request, id):
    a = student_wifi.objects.get(id=id)
    for x in student_wifi.objects.only('id').filter(g_stats1= "On process"):
        if a == x:
            x = student_wifi.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcInternet')

def StudentWifi_permit(request, id):
    a = student_wifi.objects.get(id=id)
    current_user = request.user
    for x in student_wifi.objects.only('id').filter(g_stats1= "On process"):
        if a == x:
            x = student_wifi.objects.filter(id=id).update(g_stats1="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Wifi Access has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcInternet')

def StudentInternet_cancel(request, id):
    a = student_internet.objects.get(id=id)
    for x in student_internet.objects.only('id').filter(g_stats2= "On process"):
        if a == x:
            x = student_internet.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcInternet')

def StudentInternet_permit(request, id):
    a = student_internet.objects.get(id=id)
    current_user = request.user
    for x in student_internet.objects.only('id').filter(g_stats2= "On process"):
        if a == x:
            x = student_internet.objects.filter(id=id).update(g_stats2="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Internet Access has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcInternet')

def labsched_cancel(request, id):
    if request.method == 'POST':
        a = faculty_lab.objects.get(id=id)
        for x in faculty_lab.objects.only('id').filter(l_stat= "On process"):
            if a == x:
                x = faculty_lab.objects.filter(id=id).update(l_stat="Declined")
                y = faculty_lab.objects.filter(id=id).only("f_name").values()
                for x in y:
                    print(x['f_name'])
                    name = x['f_name']
                    asd = register1.objects.filter(name=name).values()
                    for z in asd:
                        uemail = z['gsfe']
                reason = request.POST.get("reason")
                print(name)
                print(reason)
                print(uemail)
                message = "Good day " + name + ", \n Your request for Laboratory Schedule has been declined, " + reason +"\n UITC admin"
                email = EmailMessage(
                            name,
                            message,
                            'tupc.uitconlinesystem@gmail.com',
                            [uemail],

                            )

                email.send()
                break
    messages.success(request, "Successfully done")
    return redirect('/UitcLabsched')

def labsched_permit(request, id):
    a = faculty_lab.objects.get(id=id)
    current_user = request.user
    for x in faculty_lab.objects.only('id').filter(l_stat= "On process"):
        if a == x:
            x = faculty_lab.objects.filter(id=id).update(l_stat="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Laboratory Schedule has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcLabsched')

def fpasswordreset_cancel(request, id):
    a = faculty_passreset.objects.get(id=id)
    for x in faculty_passreset.objects.only('id').filter(fwstat= "On process"):
        if a == x:
            x = faculty_passreset.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcReports')

def fpasswordreset_permit(request, id):
    a = faculty_passreset.objects.get(id=id)
    current_user = request.user
    for x in faculty_passreset.objects.only('id').filter(fwstat= "On process"):
        if a == x:
            x = faculty_passreset.objects.filter(id=id).update(fwstat="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Password Reset has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcReports')

def spasswordreset_cancel(request, id):
    a = PassReset.objects.get(id=id)
    for x in PassReset.objects.only('id').filter(psstats= "On process"):
        if a == x:
            x = PassReset.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcReports')

def spasswordreset_permit(request, id):
    a = PassReset.objects.get(id=id)
    current_user = request.user
    for x in PassReset.objects.only('id').filter(psstats= "On process"):
        if a == x:
            x = PassReset.objects.filter(id=id).update(psstats="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Password Reset has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcReports')

def sborrow_cancel(request, id):
    a = borrow_record.objects.get(id=id)
    for x in borrow_record.objects.only('id').filter(i_stats5= "On process"):
        if a == x:
            x = borrow_record.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcReports')

def sborrow_permit(request, id):
    a = borrow_record.objects.get(id=id)
    current_user = request.user
    for x in borrow_record.objects.only('id').filter(i_stats5= "On process"):
        if a == x:
            x = borrow_record.objects.filter(id=id).update(i_stats5="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Borrowing has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcReports')

def fborrow_cancel(request, id):
    a = faculty_borrow.objects.get(id=id)
    for x in faculty_borrow.objects.only('id').filter(fbstat= "On process"):
        if a == x:
            x = faculty_borrow.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcReports')

def fborrow_permit(request, id):
    a = faculty_borrow.objects.get(id=id)
    current_user = request.user
    for x in faculty_borrow.objects.only('id').filter(fbstat= "On process"):
        if a == x:
            x = faculty_borrow.objects.filter(id=id).update(fbstat="Approved")
            name = current_user.name
            uemail = current_user.gsfe
            print(name)
            print(uemail)
            message = "Good day " + name + ", \n Your request for Borrowing has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [uemail],

                        )

            email.send()
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcReports')

def Index(request):
    return redirect('/')

@login_required(login_url='/Index')
def UitcHome(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1A_HOMEPAGE(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def UitcID(request):#UITC ID page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
       dataf = faculty_ID.objects.filter(f_stat = "On Process")
       return render (request, 'TupcSysApp/1B_IDS(UITC).html', {'dataf':dataf})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def UitcInternet(request):#UITC INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        datag = faculty_wifi.objects.filter(g_stat = "On Process")
        datah = student_wifi.objects.filter(g_stats1 = "On Process")
        datai = student_internet.objects.filter(g_stats2 = "On Process")
        return render (request, 'TupcSysApp/1C_INTERNET(UITC).html', {'datag':datag, 'datah':datah, 'datai':datai})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def UitcLabsched(request):#UITC LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        datal = faculty_lab.objects.filter(l_stat = "On Process")
        return render (request, 'TupcSysApp/1D_LABSCHED(UITC).html', {'datal':datal})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def UitcReports(request):#UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data = faculty_reports.objects.filter(fstat = "On Process")
        data1 = faculty_passreset.objects.filter(fwstat = "On Process") 
        data2 = PassReset.objects.filter(psstats = "On Process")
        data3 = faculty_borrow.objects.filter(fbstat = "On Process")
        data4 = borrow_record.objects.filter(i_stats5 = "On Process")
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html', {'data':data , 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, })
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
       return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
       return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

"""@login_required(login_url='/Index')
def UitcReports_borrow(request):#UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data1 = faculty_borrow.objects.filter(fbstat = "On Process")
        data2 = borrow_record.objects.filter(i_stats5 = "On Process")
        return redirect (request, ('/UitcReports'), {'data1':data1, 'data2':data2 })
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
       return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
       return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')"""

'''@login_required(login_url='/Index')
def UitcReports_borrow(request):#UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        if request.method == "POST":
            if_name5 = request.POST.get('if_name5')
            i_date5 = request.POST.get('i_date5')
            i_time5 = request.POST.get('i_time5')
            ir_borrow5 = request.POST.get('ir_borrow5')
            irf_borrow5 = request.POST.get('irf_borrow5')
            i_sig5 = request.POST.get('i_sig5')
            i_stats5 = "On Process"
            data = UITC_borrow_record.objects.create(if_name5 = if_name5, i_date5=i_date5, i_time5=i_time5, ir_borrow5=ir_borrow5, irf_borrow5=irf_borrow5, i_sig5=i_sig5, i_stats5=i_stats5)
            data.save()
        return redirect('/UitcReports')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
       return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
       return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')'''

@login_required(login_url='/Index')
def UitcReports_maitenance(request):#UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        if request.method == "POST":
            i_type4 = request.POST.get('i_type4')
            is_num4 = request.POST.get('is_num4')
            i_datem = request.POST.get('i_datem')
            i_brand4 = request.POST.get('i_brand4')
            i_code = request.POST.get('i_code')
            ie_name = request.POST.get('ie_name')
            iup_sstats = "On Process"
            i_remarks = request.POST.get('i_remarks')
            i_cobfs = request.POST.get('i_cobfs')
            i_remarks2 = request.POST.get('i_remarks2')
            iup_sstats2 = "On Process"
            i_remarks3 = request.POST.get('i_remarks3')
            i_scan = request.POST.get('i_scan')
            i_remarks4 = request.POST.get('i_remarks4')
            ia_virus = request.POST.get('ia_virus')
            i_remarks5 = request.POST.get('i_remarks5')
            im_stats = request.POST.get('im_stats')
            i_remarks6 = request.POST.get('i_remarks6')
            ik_stats = request.POST.get('ik_stats')
            i_remarks7 = request.POST.get('i_remarks7')
            i_dust = request.POST.get('i_dust')
            i_remarks8= request.POST.get('i_remarks8')
            i_organize = request.POST.get('i_organize')
            i_remarks9 = request.POST.get('i_remarks9')
            i_wipe = request.POST.get('i_wipe')
            i_remarks10 = request.POST.get('i_remarks10')
            i_run= request.POST.get('i_run')
            i_remarks11 = request.POST.get('i_remarks11')
            i_defragement = request.POST.get('i_defragement')
            i_remarks12 = request.POST.get('i_remarks12')
            i_empty = request.POST.get('i_empty')
            i_remarks13 = request.POST.get('i_remarks13')
            i_create = request.POST.get('i_create')
            i_remarks14 = request.POST.get('i_remarks14')
            iu_pers4 = request.POST.get('iu_pers4')
            i_sig4 = request.POST.get('i_sig4')
            is_date4 = request.POST.get('is_date4')
            is_time4 = request.POST.get('is_time4')
            ie_date4 = request.POST.get('ie_date4')
            ie_time4 = request.POST.get('ie_time4')
            is_rec4 = request.POST.get('is_rec4')
            ie_user4 = request.POST.get('ie_user4')
            i_sig = request.POST.get('is_num4')
            ie_date5 = request.POST.get('is_num4')
            i_time2 = request.POST.get('is_num4')
            i_stats = "On Process"
            data = maintain_record.objects.create(i_type4 = i_type4, is_num4=is_num4, 
            i_datem=i_datem, i_brand4=i_brand4, i_code=i_code, ie_name=ie_name, iup_sstats=iup_sstats,
            i_remarks = i_remarks, i_cobfs=i_cobfs, i_remarks2=i_remarks2, iup_sstats2=iup_sstats2, 
            i_remarks3=i_remarks3, i_scan=i_scan, i_remarks4=i_remarks4, ia_virus=ia_virus, 
            i_remarks5=i_remarks5, im_stats=im_stats, i_remarks6=i_remarks6, ik_stats=ik_stats,
            i_remarks7=i_remarks7, i_dust=i_dust, i_remarks8=i_remarks8, i_organize=i_organize,
            i_remarks9=i_remarks9, i_wipe=i_wipe, i_remarks10=i_remarks10, i_run=i_run, i_remarks11=i_remarks11,
            i_defragement=i_defragement, i_remarks12=i_remarks12, i_empty=i_empty, i_remarks13=i_remarks13,
            i_create=i_create, i_remarks14=i_remarks14, iu_pers4=iu_pers4, i_sig4=i_sig4, is_date4=is_date4,
            is_time4=is_time4, ie_date4=ie_date4, ie_time4=ie_time4, is_rec4=is_rec4, ie_user4=ie_user4,
            i_sig=i_sig, ie_date5=ie_date5, i_time2=i_time2, i_stats=i_stats)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return redirect('/UitcReports')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
       return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
       return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def UitcRec1(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data = faculty_ID.objects.all()
        return render (request, 'TupcSysApp/1F_RECORDS1.1(uitc).html', {'data':data})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def UitcRec2(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data1 = faculty_wifi.objects.all()
        data2 = student_wifi.objects.all()
        data3 = student_internet.objects.all()
        return render (request, 'TupcSysApp/1G_RECORDS1.2(uitc).html', {'data1':data1, 'data2':data2, 'data3':data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcRec3(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data = faculty_lab.objects.all()
        return render (request, 'TupcSysApp/1H_RECORDS1.3(uitc).html', {'data':data})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcRec4(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data1 = faculty_borrow.objects.all()
        data2 = borrow_record.objects.all()
        data3 = faculty_passreset.objects.all()
        data4 = PassReset.objects.all()
        return render (request, 'TupcSysApp/1I_RECORDS1.4(uitc).html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4,})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def UitcPermission(request):#UITC PERMISSION page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        lists = list.objects.all()
        return render (request, 'TupcSysApp/1J_PERMISSION(UITC).html',{'lists':lists})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def FacultyHome(request):#FACULTY HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1K_HOMEPAGE(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    else:
        return redirect('/')
"""def edit(request):
	cont = register1.objects.get(username="UITC00")
    cont.set_password("Anggandako28.")
	form = Registration(instance=cont)
	if request.method == 'POST':
		form = Registration(request.POST, instance = cont)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request, 'TupcSysApp/ex.html', {'form':form})"""


@login_required(login_url='/Index')
def FacultyID(request):#FACULTY ID page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            ff_name1 = request.POST.get('ff_name1')
            fm_name1 = request.POST.get('fm_name1')
            fl_name1 = request.POST.get('fl_name1')
            f_suffix1 = request.POST.get('f_suffix1')
            f_emp1 = request.POST.get('f_emp1')
            f_datereq1 = request.POST.get('f_datereq1')
            f_daterel1 = request.POST.get('f_daterel1')
            f_gsis1 = request.POST.get('f_gsis1')
            f_gsisp1 = request.POST.get('f_gsisp1')
            f_tin1 = request.POST.get('f_tin1')
            f_pagibig1 = request.POST.get('f_pagibig1')
            f_phil1 = request.POST.get('f_phil1')
            f_other1 = request.POST.get('f_other1')
            f_cp1 = request.POST.get('f_cp1')
            f_num1 = request.POST.get('f_num1')
            f_add1 = request.POST.get('f_add1')
            f_signature1 = request.POST.get('f_signature1')
            f_stat = "On Process"
            data = faculty_ID.objects.create(ff_name = ff_name1, fm_name=fm_name1, fl_name=fl_name1, f_suffix=f_suffix1, f_emp=f_emp1, 
            f_datereq=f_datereq1, f_daterel=f_daterel1, f_gsis=f_gsis1, f_gsisp=f_gsisp1, f_tin=f_tin1, f_pagibig=f_pagibig1, f_phil=f_phil1, 
            f_other=f_other1, f_cp=f_cp1, f_num=f_num1, f_add=f_add1, f_signature=f_signature1, f_stat=f_stat)
            data.save()
            messages.success(request, 'Your entry will be in queue, please wait for the admin to approve.')
        return render(request, 'TupcSysApp/1L_ID(FV).html')

    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')



@login_required(login_url='/Index')
def FacultyInternet(request):#FACULTY INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.name')
            g_dept = request.POST.get('g_dept')
            g_des = request.POST.get('g_des')
            g_sys = request.POST.get('g_sys')
            g_mac = request.POST.get('g_mac')
            g_num = request.POST.get('g_num')
            g_email = request.POST.get('g_email')
            g_fac = request.POST.get('g_fac')
            g_sig = request.POST.get('g_sig')
            g_datereq = request.POST.get('g_datereq')
            g_stats = "On Process"
            data = faculty_wifi.objects.create(gf_name = request.user.name, g_dept=g_dept, g_des=g_des, g_sys=g_sys, g_mac=g_mac, 
             g_num=g_num, g_email=g_email, g_fac=g_fac, g_sig=g_sig, g_datereq=g_datereq, g_stat=g_stats)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1M_INTERNET(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyLabsched(request):#FACULTY LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.name')
            dep = request.POST.get('dep')
            l_date = request.POST.get('l_date')
            lab_num = request.POST.get('lab_num')
            crs_sec = request.POST.get('crs_sec')
            s_time = request.POST.get('s_time')
            e_time = request.POST.get('e_time')
            fl_sig = request.POST.get('fl_sig')
            l_stat = "On Process"
            data = faculty_lab.objects.create(f_name = request.user.name, dep=dep, l_date=l_date, lab_num=lab_num, crs_sec=crs_sec, 
             s_time=s_time, e_time=e_time, fl_sig=fl_sig, l_stat = l_stat)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1N_SCHEDULE(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyReports(request):#FACULTY REPORTS page   
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            ftype = request.POST.get('ftype')
            fbrand = request.POST.get('fbrand')
            fserial = request.POST.get('fserial')
            fspecs = request.POST.get('fspecs')
            fnature = request.POST.get('fnature')
            request.POST.get('request.user.name')
            Fposjob = request.POST.get('Fposjob')
            fdep = request.POST.get('fdep')
            fdate = request.POST.get('fdate')
            ftime = request.POST.get('ftime')
            fsign = request.POST.get('fsign')
            fstat = "On Process"
            data = faculty_reports.objects.create(ftype = ftype, fbrand=fbrand, fserial=fserial, fspecs=fspecs, fnature=fnature, 
             fname=request.user.name, Fposjob=Fposjob, fdep=fdep, fdate = fdate, ftime=ftime, fsign=fsign, fstat = fstat)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1O_REPORTS(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def StudentHome(request):#STUDENT HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def FacultyRstPass(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.name')
            fwempID = request.POST.get('fwempID')
            fwIDtype = request.POST.get('fwIDtype')
            fwemail = request.POST.get('fwemail')
            fwstat = "On Process"
            data = faculty_passreset.objects.create(fwname = request.user.name, fwempID=fwempID, fwIDtype=fwIDtype, fwemail=fwemail, fwstat=fwstat)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render(request, 'TupcSysApp/1O_REPORTS(FV).HTML')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def FacultyBorrower(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.name')
            fbdate = request.POST.get('fbdate')
            fbtime = request.POST.get('fbtime')
            fbreq = request.POST.get('fbreq')
            fbreason = request.POST.get('fbreason')
            fbsign = request.POST.get('fbsign')
            fbstat = "On Process"
            data = faculty_borrow.objects.create(fbname = request.user.name, fbdate=fbdate, fbtime=fbtime, fbreq=fbreq, fbreason=fbreason, fbsign=fbsign, fbstat=fbstat)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render(request, 'TupcSysApp/1O_REPORTS(FV).HTML')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


def StudentHome(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request,'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')
     

@login_required(login_url='/Index')
def StudentInternet(request):#STUDENT INTERNET ACCESS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            g_csec2 = request.POST.get('g_csec2')
            g_snum2 = request.POST.get('g_snum2')
            g_sem2 = request.POST.get('g_sem2')
            g_or2 = request.POST.get('g_or2')
            g_num2 = request.POST.get('g_num2')
            g_email2 = request.POST.get('g_email2')
            g_add2=request.POST.get('g_add2')
            gu_name2 = request.POST.get('gu_name2')
            g_sig2=request.POST.get('g_sig2') 
            g_daterec2 = request.POST.get('g_daterec2')
            g_stats2 = "On Process"
            data = student_internet.objects.create(gf_name2 = request.user.name, g_csec2=g_csec2, 
            g_snum2=g_snum2, g_sem2=g_sem2, g_or2=g_or2, g_num2=g_num2, g_email2=g_email2,
            g_add2=g_add2, gu_name2=gu_name2, g_sig2=g_sig2, g_daterec2=g_daterec2, g_stats2=g_stats2)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1Q_INTERNET(SV).html')
    else:
        return redirect('/')
@login_required(login_url='/Index')
def StudentWifi(request):#STUDENT WIFI ACCESS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            g_csec1 = request.POST.get('g_csec1')
            g_snum1 = request.POST.get('g_snum1')
            g_sem1 = request.POST.get('g_sem1')
            g_or1 = request.POST.get('g_or1')
            g_sys1 = request.POST.get('g_sys1')
            g_mac1 = request.POST.get('g_mac1')
            g_num1 = request.POST.get('g_num1')
            g_email1 = request.POST.get('g_email1')
            g_add1=request.POST.get('g_add1')
            g_sig1=request.POST.get('g_sig1')
            g_daterec1 = request.POST.get('g_daterec1')
            g_stats1 = "On Process"
            data = student_wifi.objects.create(gf_name1 = request.user.name, g_csec1=g_csec1, 
            g_snum1=g_snum1, g_sem1=g_sem1, g_or1=g_or1, g_sys1=g_sys1, g_mac1=g_mac1, g_num1=g_num1, g_email1=g_email1,
            g_add1=g_add1, g_sig1=g_sig1, g_daterec1=g_daterec1, g_stats1=g_stats1)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1Q_INTERNET(SV).html')
    else:
        return redirect('/')
@login_required(login_url='/Index')
def StudentReports(request):#STUDENT REPORT page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            i_date5 = request.POST.get('i_date5')
            i_time5 = request.POST.get('i_time5')
            ir_borrow5 = request.POST.get('ir_borrow5')
            irf_borrow5 = request.POST.get('irf_borrow5')
            i_sig5 = request.POST.get('i_sig5')
            i_stats5 = "On Process"
            data = borrow_record.objects.create(if_name5 = request.user.name, i_date5=i_date5, 
            i_time5=i_time5, ir_borrow5=ir_borrow5, irf_borrow5=irf_borrow5, i_sig5=i_sig5, i_stats5=i_stats5,)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1R_REPORT(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def StudentReports_RequestPass(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            email = request.POST.get('email')
            emp_idno = request.POST.get('emp_idno')
            Account = request.POST.get('Account')
            psstats = "On Process"
            data = PassReset.objects.create(psname = request.user.name, email = email, emp_idno=emp_idno, 
            Account=Account, psstats=psstats)
            data.save()
            messages.info(request, 'Successfully Submitted!')
        return render (request, 'TupcSysApp/1R_REPORT(SV).html')
    else:
        return redirect('/')

@login_required(login_url='/Index')
def UitcInventory(request):#UITC ID page
    if request.user.is_authenticated:
        getDataInventory = Inventory.objects.all()
        forminventory = InventoryForm(request.POST or None)
        buy_id = request.POST.get('id')
        inventory_del = Inventory.objects.filter(id=buy_id)
        
        if request.method == 'POST':
            if forminventory.is_valid():
                messages.info(request,'Successfully Added!')
                inventory_del.delete()
                forminventory.save()
                return redirect('/UitcInventory')

        if request.method == "POST":
            messages.info(request,'Successfully Deleted!')
            inventory_del.delete()
            return redirect('/UitcInventory')

        context = {
            'inventory': getDataInventory
        }
        return render (request, 'TupcSysApp/1S_INVENTORY(UITC).html', context)
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


  



from msilib.schema import File
from django.shortcuts import render
from multiprocessing import context
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .forms import Registration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

installed_apps = ['TupcSysApp']

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

def permit(request, id):
    a = register1.objects.get(id=id)
    for x in register1.objects.only('id').filter(Status= "On process"):
        if a == x:
            x = register1.objects.filter(id=id).update(Status="Approved")
            break
    messages.success(request, "Successfully done")
    return redirect('/UitcPermission')

def register(request):#registration
    form = Registration()
    if request.method == "POST":
        image = request.POST.get("image")
        form =  Registration(request.POST)
        if form.is_valid():
            username = form['username'].value()
            image_file = pics.objects.create(
                                       
                                       pic=image, Usernamep = username
                                      )
            image_file.save()
            form.save()
            messages.success(request, 'Your entry will be in queue, please wait for the admin to approve.')
            return redirect('/')
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

        elif user is not None and user.Status == "Approved" and user.Personal_description == "Faculty Member":
            login(request, user)
            return redirect('/FacultyHome')
        elif user is not None and user.Status == "Approved" and user.Personal_description == "Student":
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

def cancel(request, id):
    a = register1.objects.get(id=id)
    for x in register1.objects.only('id').filter(Status= "On process"):
        if a == x:
            x = register1.objects.get(id=id).delete()
            break
    messages.info(request, "Successfully deleted")
    return redirect('/UitcPermission')

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

def UitcHome(request):
    return render(request, 'TupcSysApp/1A_HOMEPAGE(UITC).html')

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

#def UitcID(request):
#    return render(request, 'TupcSysApp/1B_IDS(UITC).html')

@login_required(login_url='/Index')
def UitcInternet(request):#UITC INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        datag = faculty_wifi.objects.filter(g_stat = "On Process")
        return render (request, 'TupcSysApp/1C_INTERNET(UITC).html', {'datag':datag})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcInternet(request):
#    return render(request, 'TupcSysApp/1C_INTERNET(UITC).html')

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

#def UitcLabsched(request):
#    return render(request, 'TupcSysApp/1D_LABSCHED(UITC).html')

@login_required(login_url='/Index')
def UitcReports(request):#UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
       return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
       return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcReports(request):
#    return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')

@login_required(login_url='/Index')
def UitcRec1(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1F_RECORDS1.1(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcRec1(request):
#    return render(request, 'TupcSysApp/1F_RECORDS1.1(uitc).html')

@login_required(login_url='/Index')
def UitcRec2(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1G_RECORDS1.2(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcRec2(request):
#    return render(request, 'TupcSysApp/1G_RECORDS1.2(uitc).html')

@login_required(login_url='/Index')
def UitcRec3(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1H_RECORDS1.3(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcRec3(request):
#   return render(request, 'TupcSysApp/1H_RECORDS1.3(uitc).html')

@login_required(login_url='/Index')
def UitcRec4(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1I_RECORDS1.4(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcRec4(request):
#    return render(request, 'TupcSysApp/1I_RECORDS1.4(uitc).html')

@login_required(login_url='/Index')
def UitcPermission(request):#UITC PERMISSION page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data = register1.objects.filter(Status = "On process")
        return render (request, 'TupcSysApp/1J_PERMISSION(UITC).html',{'data':data})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def UitcPermission(request):
#    return render(request, 'TupcSysApp/1J_PERMISSION(UITC).html')

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

#def FacultyHome(request):
#     return render(request,'TupcSysApp/1K_HOMEPAGE(FV).html')

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

#def FacultyID(request):
#     return render(request,'TupcSysApp/1L_ID(FV).html')


@login_required(login_url='/Index')
def FacultyInternet(request):#FACULTY INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            gf_name = request.POST.get('gf_name')
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
            data = faculty_wifi.objects.create(gf_name = gf_name, g_dept=g_dept, g_des=g_des, g_sys=g_sys, g_mac=g_mac, 
             g_num=g_num, g_email=g_email, g_fac=g_fac, g_sig=g_sig, g_datereq=g_datereq, g_stats=g_stats)
            data.save()
        return render (request, 'TupcSysApp/1M_INTERNET(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def FacultyInternet(request):
#     return render(request,'TupcSysApp/1M_INTERNET(FV).html')

@login_required(login_url='/Index')
def FacultyLabsched(request):#FACULTY LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            f_name = request.POST.get('f_name')
            dep = request.POST.get('dep')
            l_date = request.POST.get('l_date')
            lab_num = request.POST.get('lab_num')
            crs_sec = request.POST.get('crs_sec')
            s_time = request.POST.get('s_time')
            e_time = request.POST.get('e_time')
            fl_sig = request.POST.get('fl_sig')
            l_stat = "On Process"
            data = faculty_lab.objects.create(f_name = f_name, dep=dep, l_date=l_date, lab_num=lab_num, crs_sec=crs_sec, 
             s_time=s_time, e_time=e_time, fl_sig=fl_sig, l_stat = l_stat)
            data.save()
        return render (request, 'TupcSysApp/1N_SCHEDULE(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def FacultyLabsched(request):
#     return render(request,'TupcSysApp/1N_SCHEDULE(FV).html')

@login_required(login_url='/Index')
def FacultyReports(request):#FACULTY REPORTS page   
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1O_REPORTS(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#def FacultyReports(request):
#     return render(request,'TupcSysApp/1O_REPORTS(FV).html')

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

#def FacultyRstPass(request):
 #   return render(request, 'TupcSysApp/1S_PASSRESET(FV).HTML')

#def StudentHome(request):
#     return render(request,'TupcSysApp/1P_HOMEPAGE(SV).html')



@login_required(login_url='/Index')
def StudentInternet(request):#STUDENT INTERNET ACCESS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1Q_INTERNET(SV).html')
    else:
        return redirect('/')

#def StudentInternet(request):
#     return render(request,'TupcSysApp/1Q_INTERNET(SV).html')

@login_required(login_url='/Index')
def StudentReports(request):#STUDENT REPORT page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1R_REPORT(SV).html')
    else:
        return redirect('/')


#def StudentReports(request):
#     return render(request,'TupcSysApp/1R_REPORT(SV).html')
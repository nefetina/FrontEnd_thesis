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

def Document_save(request):
    if request.method=="POST":
        image = request.FILES["image"]
        idno = request.POST.get('idno')
        image_file = pics.objects.create(
                                       
                                       pic=image, idno=idno
                                      )
        image_path= image_file.pic.path
        image_path.save()
        return render(request, 'TupcSysApp/REGISTRATION.html', {"image_path":image_path})
    return render(request,  'TupcSysApp/REGISTRATION.html')

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
#@login_required(login_url='/Index')
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

##@login_required(login_url='/Index')
def UitcHome(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1A_HOMEPAGE(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    else:
        return redirect('/')

##@login_required(login_url='/Index')
def UitcID(request):#UITC ID page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
       return render (request, 'TupcSysApp/1B_IDS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')
    
#@login_required(login_url='/Index')
def UitcInternet(request):#UITC INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1C_INTERNET(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def UitcLabsched(request):#UITC LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1D_LABSCHED(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def UitcReports(request):#UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def UitcRec1(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1F_RECORDS1.1(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def UitcRec2(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1G_RECORDS1.2(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def UitcRec3(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1H_RECORDS1.3(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def UitcRec4(request):#UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1I_RECORDS1.4(uitc).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
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


#@login_required(login_url='/Index')
def FacultyHome(request):#FACULTY HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1K_HOMEPAGE(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def FacultyID(request):#FACULTY ID page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1L_ID(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def FacultyInternet(request):#FACULTY INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1M_INTERNET(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def FacultyLabsched(request):#FACULTY LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1N_SCHEDULE(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def FacultyReports(request):#FACULTY REPORTS page   
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return render (request, 'TupcSysApp/1O_REPORTS(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def StudentHome(request):#STUDENT HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def StudentInternet(request):#STUDENT INTERNET ACCESS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render (request, 'TupcSysApp/1Q_INTERNET(SV).html')
    else:
        return redirect('/')

#@login_required(login_url='/Index')
def StudentReports(request):#STUDENT REPORT page
    #if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        #return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')
    #elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        #return redirect('/FacultyHome')
    #elif request.user.is_authenticated and request.user.Personal_description == "Student":
        #return render (request, 'TupcSysApp/1R_REPORT(SV).html')
    #else:
     #   return redirect('/')
    return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html' )

from django.shortcuts import render
from django.shortcuts import redirect, render
import mysql.connector as sql
from . import views
# Create your views here.

installed_apps = ['TupcSysApp']

def index(request):#login page
    return render (request, 'TupcSysApp/LOGIN.html')

def register(request):#registration
    return render (request, 'TupcSysApp/REGISTRATION.html')

def UitcHome(request):#UITC HOMEPAGE page
    return render (request, 'TupcSysApp/1A_HOMEPAGE(UITC).html')

def UitcID(request):#UITC ID page
    return render (request, 'TupcSysApp/1B_IDS(UITC).html')

def UitcInternet(request):#UITC INTERNET page
    return render (request, 'TupcSysApp/1C_INTERNET(UITC).html')

def UitcLabsched(request):#UITC LABSCHED page
    return render (request, 'TupcSysApp/1D_LABSCHED(UITC).html')

def UitcReports(request):#UITC REPORTS page
    return render (request, 'TupcSysApp/1E_REPORTS(UITC).html')

def UitcRec1(request):#UITC HOMEPAGE page
    return render (request, 'TupcSysApp/1F_RECORDS1.1(uitc).html')


def UitcRec2(request):#UITC HOMEPAGE page
    return render (request, 'TupcSysApp/1G_RECORDS1.2(uitc).html')

def UitcRec3(request):#UITC HOMEPAGE page
    return render (request, 'TupcSysApp/1H_RECORDS1.3(uitc).html')

def UitcRec4(request):#UITC HOMEPAGE page
    return render (request, 'TupcSysApp/1I_RECORDS1.4(uitc).html')

def UitcPermission(request):#UITC PERMISSION page
    return render (request, 'TupcSysApp/1J_PERMISSION(UITC).html')

def FacultyHome(request):#FACULTY HOMEPAGE page
    return render (request, 'TupcSysApp/1K_HOMEPAGE(FV).html')

def FacultyID(request):#FACULTY ID page
    return render (request, 'TupcSysApp/1L_ID(FV).html')

def FacultyInternet(request):#FACULTY INTERNET page
    return render (request, 'TupcSysApp/1M_INTERNET(FV).html')

def FacultyLabsched(request):#FACULTY LABSCHED page
    return render (request, 'TupcSysApp/1N_SCHEDULE(FV).html')

def FacultyReports(request):#FACULTY REPORTS page
    return render (request, 'TupcSysApp/1O_REPORTS(FV).html')

def StudentHome(request):#STUDENT HOMEPAGE page
    return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')

def StudentInternet(request):#STUDENT INTERNET ACCESS page
    return render (request, 'TupcSysApp/1Q_INTERNET(SV).html')

def StudentReports(request):#STUDENT REPORT page
    return render (request, 'TupcSysApp/1R_REPORT(SV).html')

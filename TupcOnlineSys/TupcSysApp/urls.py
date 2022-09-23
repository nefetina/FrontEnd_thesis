from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'TupcSysApp'

urlpatterns =[
    path('', views.index, name='index'), 
    path('Index/', views.Index, name='Index'),
    path('permit/<int:id>', views.permit, name='permit'),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('register/', views.register, name='register'), 
    path('UitcHome/', views.UitcHome, name='UitcHome'), 
    path('UitcID/', views.UitcID, name='UitcID'), 
    path('UitcInternet/', views.UitcInternet, name='UitcInternet'), 
    path('UitcLabsched/', views.UitcLabsched, name='UitcLabsched'), 
    path('UitcReports/', views.UitcReports, name='UitcReports'), 
    path('UitcRec1/', views.UitcRec1, name='UitcRec1'), 
    path('UitcRec2/', views.UitcRec2, name='UitcRec2'), 
    path('UitcRec3/', views.UitcRec3, name='UitcRec3'), 
    path('UitcRec4/', views.UitcRec4, name='UitcRec4'), 
    path('UitcPermission/', views.UitcPermission, name='UitcPermission'), 
    path('FacultyHome/', views.FacultyHome, name='FacultyHome'), 
    path('FacultyID/', views.FacultyID, name='FacultyID'), 
    path('FacultyInternet/', views.FacultyInternet, name='FacultyInternet'), 
    path('FacultyLabsched/', views.FacultyLabsched, name='FacultyLabsched'), 
    path('FacultyReports/', views.FacultyReports, name='FacultyReports'), 
    path('StudentHome/', views.StudentHome, name='StudentHome'), 
    path('StudentInternet/', views.StudentInternet, name='StudentInternet'), 
    path('StudentReports/', views.StudentReports, name='StudentReports'), 
    path('logout/', views.logoutUser, name='logout'),

    ]
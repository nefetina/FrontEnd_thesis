from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'TupcSysApp'

urlpatterns =[
    path('', views.index, name='index'), 
    path('Index/', views.Index, name='Index'),
    path('facultyID_permit/<int:id>', views.facultyID_permit, name='facultyID_permit'),
    path('facultyID_cancel/<int:id>', views.facultyID_cancel, name='facultyID_cancel'),
    path('FacultyWifi_permit/<int:id>', views.FacultyWifi_permit, name='FacultyWifi_permit'),
    path('FacultyWifi_cancel/<int:id>', views.FacultyWifi_cancel, name='FacultyWifi_cancel'),
    path('StudentWifi_permit/<int:id>', views.StudentWifi_permit, name='StudentWifi_permit'),
    path('StudentWifi_cancel/<int:id>', views.StudentWifi_cancel, name='StudentWifi_cancel'),
    path('StudentInternet_permit/<int:id>', views.StudentInternet_permit, name='StudentInternet_permit'),
    path('StudentInternet_cancel/<int:id>', views.StudentInternet_cancel, name='StudentInternet_cancel'),
    path('labsched_permit/<int:id>', views.labsched_permit, name='labsched_permit'),
    path('labsched_cancel/<int:id>', views.labsched_cancel, name='labsched_cancel'),
    path('register/', views.register, name='register'), 
    path('UitcHome/', views.UitcHome, name='UitcHome'), 
    path('upload_csv/', views.upload_csv, name='upload_csv'), 
    path('UitcID/', views.UitcID, name='UitcID'), 
    path('UitcInternet/', views.UitcInternet, name='UitcInternet'), 
    path('UitcLabsched/', views.UitcLabsched, name='UitcLabsched'), 
    path('UitcReports/', views.UitcReports, name='UitcReports'), 
    path('UitcReports_borrow/', views.UitcReports_borrow, name='UitcReports_borrow'),
    path('UitcReports_maitenance/', views.UitcReports_maitenance, name='UitcReports_maitenance'),  
    path('UitcRec1/', views.UitcRec1, name='UitcRec1'), 
    path('UitcRec2/', views.UitcRec2, name='UitcRec2'), 
    path('UitcRec3/', views.UitcRec3, name='UitcRec3'), 
    path('UitcRec4/', views.UitcRec4, name='UitcRec4'), 
    path('UitcPermission/', views.UitcPermission, name='UitcPermission'), 
    path('UitcInventory/', views.UitcInventory, name='UitcInventory'), 
    path('FacultyHome/', views.FacultyHome, name='FacultyHome'), 
    path('FacultyID/', views.FacultyID, name='FacultyID'), 
    path('FacultyInternet/', views.FacultyInternet, name='FacultyInternet'), 
    path('FacultyLabsched/', views.FacultyLabsched, name='FacultyLabsched'), 
    path('FacultyReports/', views.FacultyReports, name='FacultyReports'),
    path('FacultyRstPass/', views.FacultyRstPass, name='FacultyRstPass'),
    path('FacultyBorrower/', views.FacultyBorrower, name='FacultyBorrower'),
    path('StudentHome/', views.StudentHome, name='StudentHome'), 
    path('StudentWifi/', views.StudentWifi, name='StudentWifi'), 
    path('StudentInternet/', views.StudentInternet, name='StudentInternet'), 
    path('StudentReports_RequestPass/', views.StudentReports_RequestPass, name='StudentReports_RequestPass'), 
    path('StudentReports/', views.StudentReports, name='StudentReports'), 
    path('logout/', views.logoutUser, name='logout'),

    ]
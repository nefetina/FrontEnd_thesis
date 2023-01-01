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
    path('fpass_cancel/<int:id>', views.fpass_cancel, name='fpass_cancel'),
    path('fpasswordreset_permit/<int:id>', views.fpasswordreset_permit, name='fpasswordreset_permit'),
    path('spasswordreset_cancel/<int:id>', views.spasswordreset_cancel, name='spasswordreset_cancel'),
    path('spasswordreset_permit/<int:id>', views.spasswordreset_permit, name='spasswordreset_permit'),
    path('sborrow_cancel/<int:id>', views.sborrow_cancel, name='sborrow_cancel'),
    path('sborrow_permit/<int:id>', views.sborrow_permit, name='sborrow_permit'),
    path('fb_cancel/<int:id>', views.fb_cancel, name='fb_cancel'),
    path('fborrow_permit/<int:id>', views.fborrow_permit, name='fborrow_permit'),
    path('maintain_cancel/<int:id>', views.maintain_cancel, name='maintain_cancel'),
    path('maintain_permit/<int:id>', views.maintain_permit, name='maintain_permit'),
    path('register/', views.register, name='register'), 
    path('employeeID_dl/<int:id>', views.employeeID_dl, name='employeeID_dl'), 
    path('internetStudent_dl/<int:id>', views.internetStudent_dl, name='internetStudent_dl'), 
    path('wifiStudent_dl/<int:id>', views.wifiStudent_dl, name='wifiStudent_dl'),
    path('Borrower_dl/<int:id>', views.Borrower_dl, name='Borrower_dl'),
    path('Borrower_dsv/<int:id>', views.Borrower_dlsv, name='Borrower_dlsv'),
    path('wifiFaculty_dl/<int:id>', views.wifiFaculty_dl, name='wifiFaculty_dl'),
    path('repair_dl/<int:id>', views.repair_dl, name='repair_dl'),
    path('maintenance_dl/<int:id>', views.maintenance_dl, name='maintenance_dl'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'), 
    path('UitcHome/', views.UitcHome, name='UitcHome'), 
    path('upload_csv/', views.upload_csv, name='upload_csv'), 
    path('upload_csv_l1/', views.upload_csv_l1, name='upload_csv_l1'), 
    path('upload_csv_l2/', views.upload_csv_l2, name='upload_csv_l2'), 
    path('upload_csv_l3/', views.upload_csv_l3, name='upload_csv_l3'), 
    path('UitcID/', views.UitcID, name='UitcID'), 
    path('UitcInternet/', views.UitcInternet, name='UitcInternet'), 
    path('UitcLabsched/', views.UitcLabsched, name='UitcLabsched'), 
    path('UitcReports/', views.UitcReports, name='UitcReports'), 
    path('UitcReports_maintenance/', views.UitcReports_maintenance, name='UitcReports_maintenance'),  
    path('UitcRec1/', views.UitcRec1, name='UitcRec1'), 
    path('UitcRec2/', views.UitcRec2, name='UitcRec2'), 
    path('UitcRec3/', views.UitcRec3, name='UitcRec3'), 
    path('UitcRec4/', views.UitcRec4, name='UitcRec4'), 
    path('UitcPermission/', views.UitcPermission, name='UitcPermission'), 
    path('UitcInventory/', views.UitcInventory, name='UitcInventory'),
    path('UitcInventory_borrowed/<int:id>', views.UitcInventory_borrowed, name='UitcInventory_borrowed'),
    path('UitcInventory_returned/<int:id>', views.UitcInventory_returned, name='UitcInventory_returned'),
    path('inventory_notify/<int:id>', views.inventory_notify, name='inventory_notify'),
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
    path('l1_delete/', views.l1_delete, name='l1_delete'),
    path('l2_delete/', views.l2_delete, name='l2_delete'),
    path('l3_delete/', views.l3_delete, name='l3_delete'),
    path('list_delete/', views.list_delete, name='list_delete'),
    path('reqrepmain_permit/<int:id>', views.reqrepmain_permit, name='reqrepmain_permit'),
    path('reqrepmain_cancel/<int:id>', views.reqrepmain_cancel, name='reqrepmain_cancel'),
    


    ]
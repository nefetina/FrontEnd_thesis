from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Registration(UserCreationForm):
    class Meta:
        model= register1    
        fields = ['gsfe', 'username', 'name', 'email', 'password1', 'password2', 'Personal_description']

class FacultyIDForm(forms.ModelForm):
	class Meta:
		model = faculty_ID
		fields = '__all__'

class FacultyWifiForm(forms.ModelForm):
	class Meta:
		model = faculty_wifi
		fields = '__all__' 

class StudentWifiForm(forms.ModelForm):
	class Meta:
		model = student_wifi
		fields = '__all__'

class StudentInternetForm(forms.ModelForm):
	class Meta:
		model = student_internet
		fields = '__all__' 

class ScheduleRecordForm(forms.ModelForm):
	class Meta:
		model = sched_rec
		fields = '__all__'

class RepairandMaintenanceRecordForm(forms.ModelForm):
	class Meta:
		model = repmain_rec
		fields = '__all__'

class MaintenanceRecordForm(forms.ModelForm):
	class Meta:
		model = maintain_record
		fields = '__all__'

class BorrowRecordForm(forms.ModelForm):
	class Meta:
		model = borrow_record
		fields = '__all__'






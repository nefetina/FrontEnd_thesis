from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		fields = '__all__'


class Registration(UserCreationForm):
    class Meta:
        model= register1    
        fields = ['gsfe', 'username', 'name', 'email', 'password1', 'password2']

class form_list(forms.ModelForm):
	class Meta:
		model = list
		fields = ['lgsfe', 'lidno', 'type']

class Faculty_report(forms.ModelForm):
	class Meta:
		model = faculty_reports
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


class MaintenanceRecordForm(forms.ModelForm):
	class Meta:
		model = maintain_record
		fields = '__all__'

class BorrowRecordForm(forms.ModelForm):
	class Meta:
		model = borrow_record
		fields = '__all__'

class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = '__all__'





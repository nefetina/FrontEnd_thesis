import logging
from django.utils import timezone
from datetime import datetime
from time import strftime

from .models import register1
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .forms import Registration
from .models import *

from django.db.models import Count

from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

import base64
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
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


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return redirect('/UitcPermission', data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('/UitcPermission')
    # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (
                csv_file.size/(1000*1000),))
            return redirect('/UitcPermission')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        # loop over the lines and save them in db. If error , store as string and then display
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
                    logging.getLogger("error_logger").error(
                        form.errors.as_json())
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        pass
        return redirect('/UitcPermission')


def upload_csv_l1(request):
    data = {}
    if "GET" == request.method:
        return redirect('/UitcLabsched', data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('/UitcLabsched')
    # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (
                csv_file.size/(1000*1000),))
            return redirect('/UitcLabsched')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        # loop over the lines and save them in db. If error , store as string and then display
        for line in lines:
            fields = line.split(",")
            data_dict = {}
            data_dict['lubnum'] = request.POST.get("lubnum")
            data_dict['ldate'] = request.POST.get("ldate")
            data_dict["lmon"] = fields[0]
            data_dict["ltue"] = fields[1]
            data_dict["lwed"] = fields[2]
            data_dict["lthu"] = fields[3]
            data_dict["lfri"] = fields[4]

            try:
                form = form_list_l1(data_dict)
                if form.is_valid():
                    form.save()
                    messages.warning(request, "Submitted")
                else:
                    logging.getLogger("error_logger").error(
                        form.errors.as_json())
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        pass
        return redirect('/UitcLabsched')


def l1_delete(request, id):
    a = Schedule_lab.objects.get(id=id)
    sched = request.POST.get("lnum")
    for x in Schedule_lab.objects.only('id'):
        if a == x:
            Schedule_lab.objects.filter(lubnum=sched).delete()
    print(sched)
    messages.info(request, "Deleted!")
    return redirect('/UitcLabsched')


def list_delete(request):
    list.objects.all().delete()
    return redirect('/UitcPermission')
# download html button


def employeeID_dl(request, id):
    data = faculty_ID.objects.filter(id=id)
    return render(request, 'TupcSysApp/4AEMPLOYEEID.html', {'data': data})


def internetStudent_dl(request, id):
    data3 = student_internet.objects.filter(id=id)
    return render(request, 'TupcSysApp/4BINTERNETACCESS(sv).html', {'data3': data3})


def wifiStudent_dl(request, id):
    data2 = student_wifi.objects.filter(id=id)
    return render(request, 'TupcSysApp/4CWIFICON(sv).html', {'data2': data2})


def Borrower_dl(request, id):
    data1 = borrow_record.objects.filter(id=id)
    return render(request, 'TupcSysApp/4DBORROWERSFORM(fv).html', {'data1': data1})


def Borrower_dlsv(request, id):
    data1 = borrow_record.objects.filter(id=id)
    return render(request, 'TupcSysApp/4DBORROWERSFORM(sv).html', {'data1': data1})


def wifiFaculty_dl(request, id):
    data1 = faculty_wifi.objects.filter(id=id)
    return render(request, 'TupcSysApp/4EWIFICON(fv).html', {'data1': data1})


def maintenance_dl(request, id):
    data1 = maintain_record.objects.filter(id=id)
    return render(request, 'TupcSysApp/4FMAINTENANCE.html', {'data1': data1})


def repair_dl(request, id):
    data1 = faculty_reports.objects.filter(id=id)
    return render(request, 'TupcSysApp/4GREQUESTREPAIR.html', {'data1': data1})


def ID_dl(request, id):
    data1 = faculty_ID.objects.filter(id=id)
    return render(request, 'TupcSysApp/4HID(fv).html', {'data1': data1})


def register(request):  # registration
    form = Registration()
    a = list.objects.all()
    if request.method == "POST":

        b = request.POST.get("username")
        c = request.POST.get("gsfe")
        d = request.POST.get("password1")
        e = request.POST.get("password2")
        ccc = list.objects.only('id').filter(lidno=b)
        y = ccc.values()
        for x in y:
            print(x['type'])
            type = x['type']
            lgsfe = x['lgsfe']
            ids = x['id']

            if x["lidno"] == b and x['lgsfe'] == c:
                form = Registration(request.POST)
                # form["Personal_description"].value = c
                if form.is_valid():
                    form.save()
                    register1.objects.filter(username=b).update(
                        Personal_description=type)
                    messages.success(
                        request, 'You are now successfully registered')
                    # email
                    name = form["name"].value()
                    message = "You are succesfully registered as " + \
                        type + "! \n Your Username is " + b + '.'
                    email = EmailMessage(
                        name,
                        message,
                        'tupc.uitconlinesystem@gmail.com',
                        [lgsfe],

                    )

                    email.send()

                    return redirect('/')
                if d != e:
                    messages.warning(request, "Password Not Match")
                else:
                    messages.warning(request, "Recheck all your input info")

            else:
                messages.warning(request, "Recheck all your input info")

    context = {
        'form': form,
        'data1': a
    }

    return render(request, 'TupcSysApp/REGISTRATION.html', context)


def index(request):  # login page
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
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

    return render(request, 'TupcSysApp/LOGIN.html')


@login_required(login_url='/Index')
def logoutUser(request):
    logout(request)
    request.user.Personal_description = None
    return redirect('/')


def maintain_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_reports.objects.filter(id=id).only("ie_user").values()
        for z in y:
            name = z['ie_user']

        adm = datetime.now()
        faculty_reports.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + name + ",\nYou approved " + name + "\nrequest for repair and maintence at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nOther details will be provided by " + name + ",\nand it will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = maintain_record.objects.get(id=id)
    for x in maintain_record.objects.only('id').filter(i_stats="On process"):
        if a == x:
            x = maintain_record.objects.filter(
                id=id).update(i_stats="Approved")
        name = request.user.name
        uemail = request.user.email
        print("asd")
        message = "Good day " + name + \
            ", \n Your request for repair and maintence has been approved." + "\n UITC admin"
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


def maintain_cancel(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_reports.objects.filter(id=id).only("ie_user").values()
        for z in y:
            name = z['ie_user']

        adm = datetime.now()
        faculty_reports.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + name + ",\nYou declined " + name + "\nrequest for repair and maintenance at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = maintain_record.objects.get(id=id)
        reason = request.POST.get("reasonm")
        for x in maintain_record.objects.only('id').filter(i_stats="On process"):
            if a == x:
                x = maintain_record.objects.filter(
                    id=id).update(i_stats="Declined")
                name = request.user.name
                uemail = request.user.email
                print(reason)
                message = "Good day " + name + \
                    ", \n Your request for repair and maintence has been declined, " + \
                    reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Completed")
    return redirect('/UitcReports')


def facultyID_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_ID.objects.filter(id=id).only("ff_name").values()
        for z in y:
            name = z['ff_name']

        adm = datetime.now()
        faculty_ID.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for ID at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()

    a = faculty_ID.objects.get(id=id)
    data1 = faculty_ID.objects.filter(id=id)
    for x in faculty_ID.objects.only('id').filter(f_stat="On process"):
        if a == x:
            x = faculty_ID.objects.filter(id=id).update(f_stat="Approved")
            y = faculty_ID.objects.filter(id=id).values()
            for z in y:
                name = z['ff_name']
                uemail = z['email1']
            message = "Good day " + name + \
                ", \n Your request for Evaluation of ID has been approved, please proceed to UITC. \n UITC admin"
            email = EmailMessage(
                name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [uemail],

            )

            email.send()
            break
    messages.success(request, "Successfully done")
    return render(request, 'TupcSysApp/4HID.html', {'data1': data1})


def facultyID_cancel(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_ID.objects.filter(id=id).only("ff_name").values()
        for z in y:
            name = z['ff_name']

        adm = datetime.now()
        faculty_ID.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for ID at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = faculty_ID.objects.get(id=id)
    reason = request.POST.get("reason")
    for x in faculty_ID.objects.only('id').filter(f_stat="On process"):
        if a == x:
            x = faculty_ID.objects.filter(id=id).update(f_stat="Declined")
            y = faculty_ID.objects.filter(id=id).values()
            for z in y:
                name = z['ff_name']
                uemail = z['email1']
                print(name)
                print(uemail)
            break

    message = "Good day " + name + \
        ", \n Your request for ID request has been declined, " + reason + "\n UITC admin"
    email = EmailMessage(
        name,
        message,
        'tupc.uitconlinesystem@gmail.com',
        [uemail],

    )

    email.send()

    messages.info(request, "Completed")
    return redirect('/UitcID')


def FacultyWifi_cancel(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_wifi.objects.filter(id=id).only("gf_name").values()
        for z in y:
            name = z['gf_name']

        adm = datetime.now()
        faculty_wifi.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Wifi Access at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = faculty_wifi.objects.get(id=id)
        reason = request.POST.get("reason1")
        for x in faculty_wifi.objects.only('id').filter(g_stat="On process"):
            if a == x:
                x = faculty_wifi.objects.filter(
                    id=id).update(g_stat="Declined")
                y = faculty_wifi.objects.filter(id=id).values()
                for z in y:
                    name = z['gf_name']
                    uemail = z['g_email']
                    print(name)
                    print(uemail)
                print(reason)
                message = "Good day " + name + \
                    ", \n Your request for Wifi request has been declined, " + reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Completed")
    return redirect('/UitcInternet')


def FacultyWifi_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_wifi.objects.filter(id=id).only("gf_name").values()
        for z in y:
            name = z['gf_name']

        adm = datetime.now()
        faculty_wifi.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Wifi Access at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = faculty_wifi.objects.get(id=id)
    for x in faculty_wifi.objects.only('id').filter(g_stat="On process"):
        if a == x:
            x = faculty_wifi.objects.filter(id=id).update(g_stat="Approved")
            y = faculty_wifi.objects.filter(id=id).values()
            for z in y:
                name = z['gf_name']
                uemail = z['g_email']
            message = "Good day " + name + \
                ", \n Your request for Wifi Access has been approved, please proceed to UITC. \n UITC admin"
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
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = student_wifi.objects.filter(id=id).only("gf_name1").values()
        for z in y:
            name = z['gf_name1']

        adm = datetime.now()
        student_wifi.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Wifi Access at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = student_wifi.objects.get(id=id)
        reason = request.POST.get("reason2")
        for x in student_wifi.objects.only('id').filter(g_stats1="On process"):
            if a == x:
                x = student_wifi.objects.filter(
                    id=id).update(g_stats1="Declined")
                y = student_wifi.objects.filter(id=id).values()
                for z in y:
                    name = z['gf_name1']
                    uemail = z['g_email1']
                    print(name)
                    print(uemail)
                print(reason)
                message = "Good day " + name + \
                    ", \n Your request for Wifi request has been declined, " + reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Completed")
    return redirect('/UitcInternet')


def StudentWifi_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = student_wifi.objects.filter(id=id).only("gf_name1").values()
        for z in y:
            name = z['gf_name1']

        adm = datetime.now()
        student_wifi.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Wifi Access at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = student_wifi.objects.get(id=id)
    for x in student_wifi.objects.only('id').filter(g_stats1="On process"):
        if a == x:
            x = student_wifi.objects.filter(id=id).update(g_stats1="Declined")
            y = student_wifi.objects.filter(id=id).values()
            for z in y:
                name = z['gf_name1']
                uemail = z['g_email1']
            message = "Good day " + name + \
                ", \n Your request for Wifi Access has been approved, please proceed to UITC. \n UITC admin"
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
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = student_internet.objects.filter(id=id).only("gf_name2").values()
        for z in y:
            name = z['gf_name2']

        adm = datetime.now()
        student_internet.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Internet Access at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = student_internet.objects.get(id=id)
        reason = request.POST.get("reason3")
        for x in student_internet.objects.only('id').filter(g_stats2="On process"):
            if a == x:
                x = student_internet.objects.filter(
                    id=id).update(g_stats2="Declined")
                y = student_internet.objects.filter(id=id).values()
                for z in y:
                    name = z['gf_name2']
                    uemail = z['g_email2']
                    print(name)
                    print(uemail)
                print(reason)
                message = "Good day " + name + \
                    ", \n Your request for Internet Access request has been declined, " + \
                    reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Completed")
    return redirect('/UitcInternet')


def StudentInternet_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = student_internet.objects.filter(id=id).only("gf_name2").values()
        for z in y:
            name = z['gf_name2']

        adm = datetime.now()
        student_internet.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Internet Access at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = student_internet.objects.get(id=id)
    for x in student_internet.objects.only('id').filter(g_stats2="On process"):
        if a == x:
            x = student_internet.objects.filter(
                id=id).update(g_stats2="Approved")
            y = student_internet.objects.filter(id=id).values()
            for z in y:
                name = z['gf_name2']
                uemail = z['g_email2']
                print(name)
                print(uemail)
            message = "Good day " + name + \
                ", \n Your request for Internet Access has been approved, please proceed to UITC. \n UITC admin"
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
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_lab.objects.filter(id=id).only("f_name").values()
        for z in y:
            name = z['f_name']

        adm = datetime.now()
        faculty_lab.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Laboratory Schedule at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = faculty_lab.objects.get(id=id)
        for x in faculty_lab.objects.only('id').filter(l_stat="On process"):
            if a == x:
                x = faculty_lab.objects.filter(id=id).update(l_stat="Declined")
                y = faculty_lab.objects.filter(id=id).only("f_name").values()
                for z in y:
                    name = z['f_name']
                    uemail = z['email2']
                reason = request.POST.get("reason")
                print(name)
                print(reason)
                print(uemail)
                message = "Good day " + name + \
                    ", \n Your request for Laboratory Schedule has been declined, " + \
                    reason + "\n UITC admin"
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
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_lab.objects.filter(id=id).only("f_name").values()
        for z in y:
            name = z['f_name']

        adm = datetime.now()
        faculty_lab.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Laboratory Schedule at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = faculty_lab.objects.get(id=id)
    for x in faculty_lab.objects.only('id').filter(l_stat="On process"):
        if a == x:
            x = faculty_lab.objects.filter(id=id).update(l_stat="Approved")
            y = faculty_lab.objects.filter(id=id).only("f_name").values()
            for z in y:
                name = z['f_name']
                uemail = z['email2']
            message = "Good day " + name + \
                ", \n Your request for Laboratory Schedule has been approved, please proceed to UITC. \n UITC admin"
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


def fpass_cancel(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_passreset.objects.filter(id=id).only("fwname").values()
        for z in y:
            name = z['fwname']

        adm = datetime.now()
        faculty_passreset.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Password Reset at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = faculty_passreset.objects.get(id=id)
        reason = request.POST.get("freason")
        for x in faculty_passreset.objects.only('id').filter(fwstat="On process"):
            if a == x:
                x = faculty_passreset.objects.filter(
                    id=id).update(fwstat="Declined")
                y = faculty_passreset.objects.filter(
                    id=id).only("fwname").values()
                for z in y:
                    name = z['fwname']
                    uemail = z['fwemail']

                print(name)
                print(reason)
                print(uemail)
                message = "Good day " + name + \
                    ", \n Your request for Password Reset has been declined, " + reason + "\n UITC admin"
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


def fpasswordreset_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_passreset.objects.filter(id=id).only("fwname").values()
        for z in y:
            name = z['fwname']

        adm = datetime.now()
        faculty_passreset.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Password Reset at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()

    a = faculty_passreset.objects.get(id=id)
    for x in faculty_passreset.objects.only('id').filter(fwstat="On process"):
        if a == x:
            x = faculty_passreset.objects.filter(
                id=id).update(fwstat="Approved")
            y = faculty_passreset.objects.filter(id=id).only("fwname").values()
            for z in y:
                name = z['fwname']
                uemail = z['fwemail']
            message = "Good day " + name + \
                ", \n Your request for Password Reset has been approved, please proceed to UITC. \n UITC admin"
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
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = PassReset.objects.get.objects.filter(id=id).only("psname").values()
        for z in y:
            name = z['psname']

        adm = datetime.now()
        PassReset.objects.filter(id=id).update(adm=adm)

        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Password Reset at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = PassReset.objects.get(id=id)
        for x in PassReset.objects.only('id').filter(psstats="On process"):
            if a == x:
                x = PassReset.objects.filter(id=id).update(psstats="Approved")
                y = PassReset.objects.filter(id=id).only("psname").values()
                for z in y:
                    name = z['psname']
                    uemail = z['email']
                reason = request.POST.get("sreason")
                print(name)
                print(uemail)
                message = "Good day " + name + \
                    ", \n Your request for Password Reset has been declined, " + reason + "\n UITC admin"
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


def spasswordreset_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = PassReset.objects.get.objects.filter(id=id).only("psname").values()
        for z in y:
            name = z['psname']

        adm = datetime.now()
        PassReset.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Password Reset at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = PassReset.objects.get(id=id)
    for x in PassReset.objects.only('id').filter(psstats="On process"):
        if a == x:
            x = PassReset.objects.filter(id=id).update(psstats="Approved")
            y = PassReset.objects.filter(id=id).only("psname").values()
            for z in y:
                name = z['psname']
                uemail = z['email']
            message = "Good day " + name + \
                ", \n Your request for Password Reset has been approved, please proceed to UITC. \n UITC admin"
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
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = borrow_record.objects.get.objects.filter(
            id=id).only("if_name5").values()
        for z in y:
            name = z['if_name5']

        adm = datetime.now()
        borrow_record.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Borrow at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    if request.method == 'POST':
        a = borrow_record.objects.get(id=id)
        for x in borrow_record.objects.only('id').filter(i_stats5="On process"):
            if a == x:
                x = borrow_record.objects.filter(
                    id=id).update(i_stats5="Declined")
                y = borrow_record.objects.filter(
                    id=id).only("if_name5").values()
                for z in y:
                    name = z['if_name5']
                    uemail = z['email5']
                reason = request.POST.get("reasonsb")
                print(name)
                print(uemail)
                message = "Good day " + name + \
                    ", \n Your request for Borrow has been declined, " + reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Successfully done")
    return redirect('/UitcReports')


def sborrow_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = borrow_record.objects.get.objects.filter(
            id=id).only("if_name5").values()
        for z in y:
            name = z['if_name5']

        adm = datetime.now()
        borrow_record.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Borrow at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = borrow_record.objects.get(id=id)
    for x in borrow_record.objects.only('id').filter(i_stats5="On process"):
        if a == x:
            x = borrow_record.objects.filter(id=id).update(i_stats5="Approved")
            y = borrow_record.objects.filter(id=id).only("if_name5").values()
            for z in y:
                name = z['if_name5']
                uemail = z['email5']

            print(name)
            print(uemail)
            message = "Good day " + name + \
                ", \n Your request for Borrowing has been approved, please proceed to UITC. \n UITC admin"
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


def fb_cancel(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_borrow.objects.filter(id=id).only("fbname").values()
        for z in y:
            name = z['fbname']

        adm = datetime.now()
        faculty_borrow.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou declined " + name + "\nrequest for Password Reset at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    print(faculty_borrow.objects.get(id=id))
    if request.method == 'POST':
        a = faculty_borrow.objects.get(id=id)
        for x in faculty_borrow.objects.only('id').filter(fbstat="On process"):
            if a == x:
                x = faculty_borrow.objects.filter(
                    id=id).update(fbstat="Declined")
                y = faculty_borrow.objects.filter(
                    id=id).only("fbname").values()
                for z in y:
                    name = z['fbname']
                    uemail = z['email4']
                reason = request.POST.get("reasonbf")
                print(name)
                print(reason)
                print(uemail)
                message = "Good day " + name + \
                    ", \n Your request for Borrow has been declined, " + reason + "\n UITC admin"
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


def fborrow_permit(request, id):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        request.POST.get('request.user.gsfe')
        request.POST.get('request.user.name')
        y = faculty_borrow.objects.filter(id=id).only("fbname").values()
        for z in y:
            name = z['fbname']

        adm = datetime.now()
        faculty_borrow.objects.filter(id=id).update(adm=adm)
        message = ("Good day! " + request.user.name + ",\nYou approved " + name + "\nrequest for Password Reset at the date and time of " +
                   adm.strftime("%b %d, %Y, %I:%M %p")+"."+"\nDetails will be recorded, Thankyou! ")
        email = EmailMessage(
            request.user.name,
            message,
            'tupc.uitconlinesystem@gmail.com',
            [request.user.gsfe],


        )

        email.send()
    a = faculty_borrow.objects.get(id=id)
    for x in faculty_borrow.objects.only('id').filter(fbstat="On process"):
        if a == x:
            x = faculty_borrow.objects.filter(id=id).update(fbstat="Approved")
            y = faculty_borrow.objects.filter(id=id).only("fbname").values()
            for z in y:
                name = z['fbname']
                uemail = z['email4']
            print(name)
            print(uemail)
            message = "Good day " + name + \
                ", \n Your request for Borrowing has been approved, please proceed to UITC. \n UITC admin"
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
def UitcHome(request):  # UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data2 = int(data1['Faculty_Internet']) + \
            int(data1['student_wifi']) + int(data1['student_internet'])
        data3 = int(data1['Faculty_borrow']) + int(data1['faculty_repair']) + int(data1['maintenance']) + \
            int(data1['Faculty_passreset']) + \
            int(data1['borrow_record']) + int(data1['student_PassReset'])

        return render(request, 'TupcSysApp/1A_HOMEPAGE(UITC).html', {'data1': data1, 'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    else:
        return redirect('/')


# modal
@login_required(login_url='/Index')
def UitcID(request):  # UITC ID page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        dataf = faculty_ID.objects.filter(f_stat="On Process")
        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data2 = int(data1['Faculty_Internet']) + \
            int(data1['student_wifi']) + int(data1['student_internet'])
        data3 = int(data1['Faculty_borrow']) + int(data1['faculty_repair']) + int(data1['maintenance']) + \
            int(data1['Faculty_passreset']) + \
            int(data1['borrow_record']) + int(data1['student_PassReset'])
        print(data1['Faculty_passreset'])
        print(data3)

        return render(request, 'TupcSysApp/1B_IDS(UITC).html', {'dataf': dataf, 'data1': data1, 'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcInternet(request):  # UITC INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        datag = faculty_wifi.objects.filter(g_stat="On Process")
        datah = student_wifi.objects.filter(g_stats1="On Process")
        datai = student_internet.objects.filter(g_stats2="On Process")
        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data2 = int(data1['Faculty_Internet']) + \
            int(data1['student_wifi']) + int(data1['student_internet'])
        data3 = int(data1['Faculty_borrow']) + int(data1['faculty_repair']) + int(data1['maintenance']) + \
            int(data1['Faculty_passreset']) + \
            int(data1['borrow_record']) + int(data1['student_PassReset'])

        return render(request, 'TupcSysApp/1C_INTERNET(UITC).html', {'datag': datag, 'datah': datah, 'datai': datai, 'data1': data1, 'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcLabsched(request):  # UITC LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        datal = faculty_lab.objects.filter(l_stat="On Process")
        data = faculty_lab.objects.filter(l_stat="Approved")
        datas = Schedule_lab.objects.all()
        sched = []
        lnum = []
        labnum = Schedule_lab.objects.values(
            'lubnum', 'ldate').annotate(Count('id'))
        for x in labnum:
            a = x['lubnum']
            b = x['ldate']
            lnum.append(a)
            scheds = Schedule_lab.objects.filter(lubnum=a, ldate=b).values()

            for z in scheds:
                z['lnum'] = a

            sched.append(scheds)
        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data2 = int(data1['Faculty_Internet']) + \
            int(data1['student_wifi']) + int(data1['student_internet'])
        data3 = int(data1['Faculty_borrow']) + int(data1['faculty_repair']) + int(data1['maintenance']) + \
            int(data1['Faculty_passreset']) + \
            int(data1['borrow_record']) + int(data1['student_PassReset'])

        return render(request, 'TupcSysApp/1D_LABSCHED(UITC).html', {'data': data, 'datal': datal, 'datas': datas, 'sched': sched, 'lnum': lnum, 'labnum': labnum, 'data1': data1, 'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcReports(request):  # UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data = faculty_reports.objects.filter(
            fstat="On Process") | faculty_reports.objects.filter(fstat="Approved") | faculty_reports.objects.filter(fstat="Notified")

        data1 = faculty_passreset.objects.filter(fwstat="On Process")
        data2 = PassReset.objects.filter(psstats="On Process")
        data3 = faculty_borrow.objects.filter(
            fbstat="On Process") | faculty_borrow.objects.filter(fbstat="Borrowed")
        data4 = borrow_record.objects.filter(
            i_stats5="On Process") | borrow_record.objects.filter(i_stats5="Borrowed")
        data5 = maintain_record.objects.filter(i_stats="On Process")
        inventory = Inventory.objects.filter(i_stats="Available")
        data6 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(data.count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data7 = int(data6['Faculty_Internet']) + \
            int(data6['student_wifi']) + int(data6['student_internet'])
        data8 = int(data6['Faculty_borrow']) + int(data6['faculty_repair']) + int(data6['maintenance']) + \
            int(data6['Faculty_passreset']) + \
            int(data6['borrow_record']) + int(data6['student_PassReset'])
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html', {'data': data, 'data1': data1, 'data2': data2, 'data3': data3, 'inventory': inventory, 'data4': data4, 'data5': data5, 'data6': data6, 'data7': data7, 'data8': data8})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
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
            data = UITC_borrow_record.objects.create(if_name5 = if_name5, i_date5=i_date5, i_time5=i_time5,
                                                     ir_borrow5=ir_borrow5, irf_borrow5=irf_borrow5, i_sig5=i_sig5, i_stats5=i_stats5)
            data.save()
        return redirect('/UitcReports')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
       return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
       return render (request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')'''


@login_required(login_url='/Index')
def UitcReports_maintenance(request):  # UITC REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        if request.method == "POST":
            i_type4 = request.POST.get('i_type4')
            is_num4 = request.POST.get('is_num4')
            i_datem = request.POST.get('i_datem')
            i_brand4 = request.POST.get('i_brand4')
            i_code = request.POST.get('i_code')
            ie_name = request.POST.get('ie_name')
            iup_sstats = request.POST.get('iup_sstats')
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
            i_remarks8 = request.POST.get('i_remarks8')
            i_organize = request.POST.get('i_organize')
            i_remarks9 = request.POST.get('i_remarks9')
            i_wipe = request.POST.get('i_wipe')
            i_remarks10 = request.POST.get('i_remarks10')
            i_run = request.POST.get('i_run')
            i_remarks11 = request.POST.get('i_remarks11')
            i_defragement = request.POST.get('i_defragement')
            i_remarks12 = request.POST.get('i_remarks12')
            i_empty = request.POST.get('i_empty')
            i_remarks13 = request.POST.get('i_remarks13')
            i_create = request.POST.get('i_create')
            i_remarks14 = request.POST.get('i_remarks14')
            request.POST.get('request.user.name')
            is_date4 = request.POST.get('is_date4')
            is_time4 = request.POST.get('is_time4')
            ie_date4 = request.POST.get('ie_date4')
            ie_time4 = request.POST.get('ie_time4')
            is_rec4 = request.POST.get('is_rec4')
            request.POST.get('request.user.name')
            i_sign = request.POST.get('i_sign')
            ie_date5 = request.POST.get('ie_date5')
            i_sig5 = request.POST.get('i_sig5')
            i_time2 = request.POST.get('i_time2')
            i_stats = "On Process"
            data = maintain_record.objects.create(i_type4=i_type4, is_num4=is_num4,
                                                  i_datem=i_datem, i_brand4=i_brand4, i_code=i_code, ie_name=ie_name, iup_sstats=iup_sstats,
                                                  i_remarks=i_remarks, i_cobfs=i_cobfs, i_remarks2=i_remarks2, iup_sstats2=iup_sstats2,
                                                  i_remarks3=i_remarks3, i_scan=i_scan, i_remarks4=i_remarks4, ia_virus=ia_virus,
                                                  i_remarks5=i_remarks5, im_stats=im_stats, i_remarks6=i_remarks6, ik_stats=ik_stats,
                                                  i_remarks7=i_remarks7, i_dust=i_dust, i_remarks8=i_remarks8, i_organize=i_organize,
                                                  i_remarks9=i_remarks9, i_wipe=i_wipe, i_remarks10=i_remarks10, i_run=i_run, i_remarks11=i_remarks11,
                                                  i_defragement=i_defragement, i_remarks12=i_remarks12, i_empty=i_empty, i_remarks13=i_remarks13,
                                                  i_create=i_create, i_remarks14=i_remarks14, iu_pers4=request.user.name, is_date4=is_date4,
                                                  is_time4=is_time4, ie_date4=ie_date4, ie_time4=ie_time4, is_rec4=is_rec4, ie_user4=request.user.name,
                                                  i_sign=i_sign, i_sig5=i_sig5, ie_date5=ie_date5, i_time2=i_time2, i_stats=i_stats)
            data.save()
        messages.info(request, 'Successfully Submitted!')
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcRec1(request):  # UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data2 = int(data1['Faculty_Internet']) + \
            int(data1['student_wifi']) + int(data1['student_internet'])
        data3 = int(data1['Faculty_borrow']) + int(data1['faculty_repair']) + int(data1['maintenance']) + \
            int(data1['Faculty_passreset']) + \
            int(data1['borrow_record']) + int(data1['student_PassReset'])
        data = faculty_ID.objects.all()
        return render(request, 'TupcSysApp/1F_RECORDS1.1(uitc).html', {'data': data, 'data1': data1, 'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcRec2(request):  # UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data1 = faculty_wifi.objects.all()
        data2 = student_wifi.objects.all()
        data3 = student_internet.objects.all()
        data4 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data5 = int(data4['Faculty_Internet']) + \
            int(data4['student_wifi']) + int(data4['student_internet'])
        data6 = int(data4['Faculty_borrow']) + int(data4['faculty_repair']) + int(data4['maintenance']) + \
            int(data4['Faculty_passreset']) + \
            int(data4['borrow_record']) + int(data4['student_PassReset'])
        return render(request, 'TupcSysApp/1G_RECORDS1.2(uitc).html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5, 'data6': data6})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcRec3(request):  # UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data = faculty_lab.objects.all()
        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data2 = int(data1['Faculty_Internet']) + \
            int(data1['student_wifi']) + int(data1['student_internet'])
        data3 = int(data1['Faculty_borrow']) + int(data1['faculty_repair']) + int(data1['maintenance']) + \
            int(data1['Faculty_passreset']) + \
            int(data1['borrow_record']) + int(data1['student_PassReset'])
        return render(request, 'TupcSysApp/1H_RECORDS1.3(uitc).html', {'data': data, 'data1': data1, 'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcRec4(request):  # UITC HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        data5 = Inventory.objects.values(
            'i_equip', 'i_model').annotate(Count('id'))
        data5a = Inventory.objects.values(
            'i_equip', 'i_model', 'i_stats').annotate(Count('id'))
        data5b = Inventory.objects.values(
            'i_equip', 'i_model', 'i_stats').annotate(Count('id'))
        data = {'i_equip': [], 'i_model': [],
                'id__count': [], 'c1': [], 'c2': []}
        asd = Inventory.objects.values(
            'i_equip', 'i_model').annotate(Count('id'))
        for x in data5:

            da = x['i_equip']
            db = x['i_model']
            d = x['id__count']
            data['i_equip'].append(da)
            data['i_model'].append(db)
            data['id__count'].append(d)
            print(da, db, d)

        for y in data5a:
            dq = y['i_stats']
            print(dq)
            if dq == "Available":
                d1 = x['id__count']
            elif dq == "Borrowed":
                d1 = 0
            else:
                d1 = 0
            data['c1'].append(d1)
            print(d1)

        for z in data5b:
            dqs = z['i_stats']
            print(dqs)
            if dqs == "Available":
                d2 = 0
            elif dqs == "Borrowed":
                d2 = x['id__count']
            else:
                d2 = 0

            data['c2'].append(d2)
        print(data)
        data1 = faculty_borrow.objects.all()
        data2 = borrow_record.objects.all()
        data3 = faculty_passreset.objects.all()
        data4 = PassReset.objects.all()
        # data5 = Inventory.objects.all()
        data6 = maintain_record.objects.all()
        data7 = faculty_reports.objects.all()
        d1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
              "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
              "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
              "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
              "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
              "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
              "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
              "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
              "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
              "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
              "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        d2 = int(d1['Faculty_Internet']) + \
            int(d1['student_wifi']) + int(d1['student_internet'])
        d3 = int(d1['Faculty_borrow']) + int(d1['faculty_repair']) + int(d1['maintenance']) + \
            int(d1['Faculty_passreset']) + \
            int(d1['borrow_record']) + int(d1['student_PassReset'])
        return render(request, 'TupcSysApp/1I_RECORDS1.4(uitc).html', {'d1': d1, 'd3': d3, 'd2': d2, 'data': data, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5, 'data5a': data5a, 'data5b': data5b, 'data6': data6, 'data7': data7})
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcPermission(request):  # UITC PERMISSION page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        lists = list.objects.all()
        data6 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data7 = int(data6['Faculty_Internet']) + \
            int(data6['student_wifi']) + int(data6['student_internet'])
        data8 = int(data6['Faculty_borrow']) + int(data6['faculty_repair']) + int(data6['maintenance']) + \
            int(data6['Faculty_passreset']) + \
            int(data6['borrow_record']) + int(data6['student_PassReset'])
        return render(request, 'TupcSysApp/1J_PERMISSION(UITC).html', {'lists': lists, 'data7': data7, 'data8': data8, 'data6': data6, })
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyHome(request):  # FACULTY HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        data = faculty_reports.objects.filter(fstat="On Process", email3=request.user.gsfe) | faculty_reports.objects.filter(
            fstat="Approved", email3=request.user.gsfe) | faculty_reports.objects.filter(
            fstat="Notified", email3=request.user.gsfe)

        data1 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process", email1=request.user.gsfe).count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process", g_email=request.user.gsfe).count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process", email2=request.user.gsfe).count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process", email4=request.user.gsfe).count()),
                 "faculty_repair": str(data.count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process", fwemail=request.user.gsfe).count())}
        return render(request, 'TupcSysApp/1K_HOMEPAGE(FV).html', {'data1': data1})
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return redirect('/StudentHome')
    else:
        return redirect('/')


@ login_required(login_url='/Index')
def FacultyID(request):  # FACULTY ID page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.gsfe')
            f_pic = request.POST.get('f_pics')
            ff_name1 = request.POST.get('ff_name1')
            fm_name1 = request.POST.get('fm_name1')
            fl_name1 = request.POST.get('fl_name1')
            f_suffix1 = request.POST.get('f_suffix1')
            f_emp1 = request.user.username
            f_datereq1 = datetime.now()
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
            f_signature = request.POST.get('f_signatures')
            f_dept = request.POST.get('f_dept')
            print(f_signature)
            f_stat = "On Process"
            data = faculty_ID.objects.create(f_pic=f_pic, email1=request.user.gsfe, ff_name=ff_name1, fm_name=fm_name1, fl_name=fl_name1, f_suffix=f_suffix1, f_emp=f_emp1,
                                             f_datereq=f_datereq1, f_daterel=f_daterel1, f_gsis=f_gsis1, f_gsisp=f_gsisp1, f_tin=f_tin1, f_pagibig=f_pagibig1, f_phil=f_phil1,
                                             f_other=f_other1, f_cp=f_cp1, f_num=f_num1, f_add=f_add1, f_signature=f_signature, f_stat=f_stat, f_dept=f_dept)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for ID at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.success(
                request, 'Your entry will be in queue, please wait for the admin to approve.')
            return redirect('/FacultyHome')
        return render(request, 'TupcSysApp/1L_ID(FV).html')

    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyInternet(request):  # FACULTY INTERNET page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.name')
            g_dept = request.POST.get('g_dept')
            g_des = request.POST.get('g_des')
            g_sys = request.POST.get('g_sys')
            g_mac = request.POST.get('g_mac')
            g_num = request.POST.get('g_num')
            request.POST.get('request.user.gsfe')
            g_fac = request.POST.get('g_fac')
            g_sig = request.POST.get('g_sig')
            g_datereq = datetime.now()
            g_stats = "On Process"
            data = faculty_wifi.objects.create(gf_name=request.user.name, g_dept=g_dept, g_des=g_des, g_sys=g_sys, g_mac=g_mac,
                                               g_num=g_num, g_email=request.user.gsfe, g_fac=g_fac, g_sig=g_sig, g_datereq=g_datereq, g_stat=g_stats)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Internet Access at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/FacultyHome')
        return render(request, 'TupcSysApp/1M_INTERNET(FV).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyLabsched(request):  # FACULTY LABSCHED page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        datas = Schedule_lab.objects.all()
        sched = []
        lnum = []
        labnum = Schedule_lab.objects.values(
            'lubnum', 'ldate').annotate(Count('id'))
        for x in labnum:
            a = x['lubnum']
            b = x['ldate']
            lnum.append(a)
            scheds = Schedule_lab.objects.filter(lubnum=a, ldate=b).values()
            for z in scheds:
                z['lnum'] = a
            sched.append(scheds)

        if request.method == "POST":
            request.POST.get('request.user.gsfe')
            request.POST.get('request.user.name')
            dep = request.POST.get('dep')
            l_date = request.POST.get('l_date')
            lab_num = request.POST.get('lab_num')
            crs_sec = request.POST.get('crs_sec')
            s_time = request.POST.get('s_time')
            e_time = request.POST.get('e_time')
            fl_sig = request.POST.get('fl_sig')
            l_stat = "On Process"
            data = faculty_lab.objects.create(email2=request.user.gsfe, f_name=request.user.name, dep=dep, l_date=l_date, lab_num=lab_num, crs_sec=crs_sec,
                                              s_time=s_time, e_time=e_time, fl_sig=fl_sig, l_stat=l_stat)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Laboratory Schedule at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/FacultyHome')
        return render(request, 'TupcSysApp/1N_SCHEDULE(FV).html', {'sched': sched, 'datas': datas, 'sched': sched, 'lnum': lnum, 'labnum': labnum})
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyReports(request):  # FACULTY REPORTS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        data1 = faculty_reports.objects.filter(fstat="On Process", email3=request.user.gsfe) | faculty_reports.objects.filter(
            fstat="Approved", email3=request.user.gsfe) | faculty_reports.objects.filter(
            fstat="Notified", email3=request.user.gsfe)
        data2 = data1.count()
        data3 = faculty_reports.objects.filter(fstat="On Process", email3=request.user.gsfe) | faculty_reports.objects.filter(
            fstat="Approved", email3=request.user.gsfe) | faculty_reports.objects.filter(
            fstat="Notified", email3=request.user.gsfe)
        if request.method == "POST":
            email3 = request.user.gsfe
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
            data = faculty_reports.objects.create(ftype=ftype, email3=email3, fbrand=fbrand, fserial=fserial, fspecs=fspecs, fnature=fnature,
                                                  fname=request.user.name, Fposjob=Fposjob, fdep=fdep, fdate=fdate, ftime=ftime, fsign=fsign, fstat=fstat)
            data.save()

            messages.info(request, 'Successfully Submitted!')
            return redirect('/FacultyHome')
        return render(request, 'TupcSysApp/1O_REPORTS(FV).html', {'data2': data2, 'data3': data3})
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def StudentHome(request):  # STUDENT HOMEPAGE page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        data1 = {"student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html', {'data1': data1})
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyRstPass(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":
            request.POST.get('request.user.name')
            fwempID = request.user.username
            fwIDtype = request.POST.get('fwIDtype')
            request.POST.get('request.user.gsfe')
            fwstat = "On Process"
            data = faculty_passreset.objects.create(
                fwname=request.user.name, fwempID=fwempID, fwIDtype=fwIDtype, fwemail=request.user.gsfe, fwstat=fwstat)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Password Reset at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/FacultyHome')
        return render(request, 'TupcSysApp/1O_REPORTS(FV).HTML')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def FacultyBorrower(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return redirect('/UitcHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        if request.method == "POST":

            request.POST.get('request.user.name')
            fbdate = datetime.now()
            fbtime = datetime.now().time()
            fbreq = request.POST.get('fbreq')
            fbreason = request.POST.get('fbreason')
            fbsign = request.POST.get('fbsign')
            fbstat = "On Process"
            print(fbtime)
            data = faculty_borrow.objects.create(email4=request.user.gsfe, fbname=request.user.name, fbdate=fbdate,
                                                 fbtime=fbtime, fbreq=fbreq, fbreason=fbreason, fbsign=fbsign, fbstat=fbstat)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Borrow at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()

            messages.info(request, 'Successfully Submitted!')
            return redirect('/FacultyHome')
        return render(request, 'TupcSysApp/1O_REPORTS(FV).HTML')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def StudentInternet(request):  # STUDENT INTERNET ACCESS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            g_csec2 = request.POST.get('g_csec2')
            g_snum2 = request.user.username
            g_sem2 = request.POST.get('g_sem2')
            g_or2 = request.POST.get('g_or2')
            g_num2 = request.POST.get('g_num2')
            request.POST.get('request.user.gsfe')
            g_add2 = request.POST.get('g_add2')
            gu_name2 = request.POST.get('gu_name2')
            g_sig2 = request.POST.get('g_sig2')
            g_daterec2 = datetime.now()
            g_stats2 = "On Process"
            data = student_internet.objects.create(gf_name2=request.user.name, g_csec2=g_csec2,
                                                   g_snum2=g_snum2, g_sem2=g_sem2, g_or2=g_or2, g_num2=g_num2, g_email2=request.user.gsfe,
                                                   g_add2=g_add2, gu_name2=gu_name2, g_sig2=g_sig2, g_daterec2=g_daterec2, g_stats2=g_stats2)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Internet Access at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/StudentHome')
        return render(request, 'TupcSysApp/1Q_INTERNET(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def StudentWifi(request):  # STUDENT WIFI ACCESS page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            g_csec1 = request.POST.get('g_csec1')
            g_snum1 = request.user.username
            g_sem1 = request.POST.get('g_sem1')
            g_or1 = request.POST.get('g_or1')
            g_sys1 = request.POST.get('g_sys1')
            g_mac1 = request.POST.get('g_mac1')
            g_num1 = request.POST.get('g_num1')
            request.POST.get('request.user.gsfe')
            g_add1 = request.POST.get('g_add1')
            g_sig1 = request.POST.get('g_sig1')
            g_daterec1 = datetime.now()
            g_stats1 = "On Process"
            data = student_wifi.objects.create(gf_name1=request.user.name, g_csec1=g_csec1,
                                               g_snum1=g_snum1, g_sem1=g_sem1, g_or1=g_or1, g_sys1=g_sys1, g_mac1=g_mac1, g_num1=g_num1, g_email1=request.user.gsfe,
                                               g_add1=g_add1, g_sig1=g_sig1, g_daterec1=g_daterec1, g_stats1=g_stats1)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Wifi Access at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/StudentHome')
        return render(request, 'TupcSysApp/1Q_INTERNET(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def StudentReports(request):  # STUDENT REPORT page
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            ir_borrow5 = []
            request.POST.get('request.user.gsfe')
            request.POST.get('request.user.name')
            i_date5 = datetime.now()
            i_time5 = datetime.now().time()
            ir_borrow5 = request.POST.get('ir_borrow5')
            irf_borrow5 = request.POST.get('irf_borrow5')
            i_sig5 = request.POST.get('i_sig5')
            i_stats5 = "On Process"
            data = borrow_record.objects.create(email5=request.user.gsfe, if_name5=request.user.name, i_date5=i_date5,
                                                i_time5=i_time5, ir_borrow5=ir_borrow5, irf_borrow5=irf_borrow5, i_sig5=i_sig5, i_stats5=i_stats5,)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Borrow at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/StudentHome')
        return render(request, 'TupcSysApp/1R_REPORT(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def StudentReports_RequestPass(request):
    if request.user.is_authenticated and request.user.Personal_description == "UITC Staff":
        return render(request, 'TupcSysApp/1E_REPORTS(UITC).html')
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        if request.method == "POST":
            request.POST.get('request.user.name')
            request.POST.get('request.user.gsfe')
            emp_idno = request.user.username
            Account = request.POST.get('Account')
            psstats = "On Process"
            data = PassReset.objects.create(psname=request.user.name, email=request.user.gsfe, emp_idno=emp_idno,
                                            Account=Account, psstats=psstats)
            data.save()
            x = datetime.now()
            message = ("Good day " + request.user.name + ",\nYour request for Password Reset at the date and time of " +
                       x.strftime("%b %d, %Y, %I:%M %p") + " has been submitted. \n -UITC admin")
            email = EmailMessage(
                request.user.name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [request.user.gsfe],


            )

            email.send()
            messages.info(request, 'Successfully Submitted!')
            return redirect('/StudentHome')
        return render(request, 'TupcSysApp/1R_REPORT(SV).html')
    else:
        return redirect('/')


@login_required(login_url='/Index')
def UitcInventory(request):  # UITC ID page
    data = faculty_borrow.objects.filter(fbstat="Approved")
    data1 = borrow_record.objects.filter(i_stats5="Approved")
    if request.user.is_authenticated:
        getDataInventory = Inventory.objects.all()
        forminventory = InventoryForm(request.POST or None)
        buy_id = request.POST.get('id')
        inventory_del = Inventory.objects.filter(id=buy_id)

        if request.method == 'POST':
            if forminventory.is_valid():
                messages.info(request, 'Successfully Added!')
                forminventory.save()
                return redirect('/UitcInventory')
        data6 = {"Faculty_ID": str(faculty_ID.objects.filter(f_stat="On Process").count()),
                 "Faculty_Internet": str(faculty_wifi.objects.filter(g_stat="On Process").count()),
                 "Faculty_Laboratory": str(faculty_lab.objects.filter(l_stat="On Process").count()),
                 "Faculty_borrow": str(faculty_borrow.objects.filter(fbstat="On Process").count()),
                 "faculty_repair": str(faculty_reports.objects.filter(fstat="On Process").count()),
                 "maintenance": str(maintain_record.objects.filter(i_stats="On Process").count()),
                 "Faculty_passreset": str(faculty_passreset.objects.filter(fwstat="On Process").count()),
                 "student_wifi": str(student_wifi.objects.filter(g_stats1="On Process").count()),
                 "student_internet": str(student_internet.objects.filter(g_stats2="On Process").count()),
                 "borrow_record": str(borrow_record.objects.filter(i_stats5="On Process").count()),
                 "student_PassReset": str(PassReset.objects.filter(psstats="On Process").count()), }

        data7 = int(data6['Faculty_Internet']) + \
            int(data6['student_wifi']) + int(data6['student_internet'])
        data8 = int(data6['Faculty_borrow']) + int(data6['faculty_repair']) + int(data6['maintenance']) + \
            int(data6['Faculty_passreset']) + \
            int(data6['borrow_record']) + int(data6['student_PassReset'])
        context = {
            'inventory': getDataInventory,
            'data': data,
            'data1': data1,
            'data6': data6,
            'data7': data7,
            'data8': data8
        }
        return render(request, 'TupcSysApp/1S_INVENTORY(UITC).html', context)
    elif request.user.is_authenticated and request.user.Personal_description == "Faculty Member":
        return redirect('/FacultyHome')
    elif request.user.is_authenticated and request.user.Personal_description == "Student":
        return render(request, 'TupcSysApp/1P_HOMEPAGE(SV).html')
    else:
        return redirect('/')


def inventory_notify(request, id):

    for y in faculty_borrow.objects.filter(id=id).values():
        i_model = y['fbmodel']
        i_serial = y['fbserial']
        user = y['fbuser']
    for y in borrow_record.objects.filter(id=id).values():
        i_model1 = y['imodel']
        i_serial1 = y['iserial']
        user = y['i_user']
    mes = request.POST.get("message")
    print(mes)

    if user == "Faculty Member":
        f = faculty_borrow.objects.filter(
            id=id, fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed").values()
        for f1 in f:
            name = f1['fbname']
            emails = f1['email4']

            message = ("Good day " + name + ", \n" +
                       mes + "\n UITC admin")
            email = EmailMessage(
                name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [emails],

            )

            email.send()
    if user == "Student":
        s = borrow_record.objects.filter(
            id=id, imodel=i_model1, iserial=i_serial1, i_stats5="Borrowed").values()
        for s1 in s:

            name = s1['if_name5']
            emails = s1['email5']
            message = ("Good day " + name + ", \n" +
                       mes + "\n UITC admin")
            email = EmailMessage(
                name,
                message,
                'tupc.uitconlinesystem@gmail.com',
                [emails],

            )

            email.send()

    messages.info(request, "Completed")
    return redirect('/UitcReports')


def UitcInventory_borrowed(request, id):
    a = Inventory.objects.get(id=id)
    fid = request.POST.get("b_id")

    print(fid)
    for y in Inventory.objects.filter(id=id).values():
        i_model = y['i_model']
        i_serial = y['i_serial']
    print(i_model)
    for x in Inventory.objects.only('id').filter(i_stats="Available"):
        if a == x:
            Inventory.objects.filter(id=id).update(i_stats="Borrowed")

            faculty_borrow.objects.filter(id=fid).update(
                fbrdate=datetime.now(), fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed")
            borrow_record.objects.filter(id=fid).update(
                i_rdate5=datetime.now(), imodel=i_model, iserial=i_serial, i_stats5="Borrowed")

    messages.success(request, "Successfully done")
    return redirect('/UitcReports')


def UitcInventory_returned(request, id):
    for y in faculty_borrow.objects.filter(id=id).values():
        i_model = y['fbmodel']
        i_serial = y['fbserial']
        user = y['fbuser']
    for y in borrow_record.objects.filter(id=id).values():
        i_model1 = y['imodel']
        i_serial1 = y['iserial']
        user = y['fbuser']
    remarks = request.POST.get("remarks")
    print(remarks)
    if request.method == "POST":
        if remarks == "Good Condition":
            Inventory.objects.filter(
                i_model=i_model, i_serial=i_serial, i_stats="Borrowed").update(i_stats="Available")
            if user == "Faculty Member":
                faculty_borrow.objects.filter(fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed").update(
                    fbremarks=remarks, fbrdate=datetime.now(), fbstat="Returned")
            elif user == "Student":
                borrow_record.objects.filter(imodel=i_model1, iserial=i_serial1, i_stats5="Borrowed").update(
                    i_remarks=remarks, i_rdate5=datetime.now(), i_stats5="Returned")
        elif remarks == "Broken":
            Inventory.objects.filter(
                i_model=i_model, i_serial=i_serial, i_stats="Borrowed").update(i_stats="Broken")
            if user == "Faculty Member":
                faculty_borrow.objects.filter(fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed").update(
                    fbremarks=remarks, fbrdate=datetime.now(), fbstat="Returned")
            elif user == "Student":
                borrow_record.objects.filter(imodel=i_model1, iserial=i_serial1, i_stats5="Borrowed").update(
                    i_remarks=remarks, i_rdate5=datetime.now(), i_stats5="Returned")
        elif remarks == "Replaced":
            Inventory.objects.filter(
                i_model=i_model, i_serial=i_serial, i_stats="Borrowed").update(i_stats="Replaced")
            if user == "Faculty Member":
                faculty_borrow.objects.filter(fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed").update(
                    fbremarks=remarks, fbrdate=datetime.now(), fbstat="Returned")
            elif user == "Student":
                borrow_record.objects.filter(imodel=i_model1, iserial=i_serial1, i_stats5="Borrowed").update(
                    i_remarks=remarks, i_rdate5=datetime.now(), i_stats5="Returned")
        elif remarks == "Missing some parts":
            Inventory.objects.filter(i_model=i_model, i_serial=i_serial, i_stats="Borrowed").update(
                i_stats="Missing some parts")
            if user == "Faculty Member":
                faculty_borrow.objects.filter(fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed").update(
                    fbremarks=remarks, fbrdate=datetime.now(), fbstat="Returned")
            elif user == "Student":
                borrow_record.objects.filter(imodel=i_model1, iserial=i_serial1, i_stats5="Borrowed").update(
                    i_remarks=remarks, i_rdate5=datetime.now(), i_stats5="Returned")
        elif remarks == "Not working":
            Inventory.objects.filter(
                i_model=i_model, i_serial=i_serial, i_stats="Borrowed").update(i_stats="Not working")
            if user == "Faculty Member":
                faculty_borrow.objects.filter(fbmodel=i_model, fbserial=i_serial, fbstat="Borrowed").update(
                    fbremarks=remarks, fbrdate=datetime.now(), fbstat="Returned")
            elif user == "Student":
                borrow_record.objects.filter(imodel=i_model1, iserial=i_serial1, i_stats5="Borrowed").update(
                    i_remarks=remarks, i_rdate5=datetime.now(), i_stats5="Returned")

    messages.success(request, "Successfully done")
    return redirect('/UitcReports')


def forgotpassword(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = register1.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "TupcSysApp/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'TupcSysApp',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'tupc.uitconlinesystem@gmail.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(
                        request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect('/')
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request, 'TupcSysApp/FORGOT_PASS.html', context={"password_reset_form": password_reset_form})


def UitcInventory_modify(request, id):
    a = Inventory.objects.get(id=id)

    for y in Inventory.objects.filter(id=id).values():
        i_model = y['i_model']
        i_serial = y['i_serial']
    print(i_model)
    print(i_serial)
    remarks = request.POST.get("remarks")
    print(remarks)
    for x in Inventory.objects.only('id'):
        if a == x:
            if remarks == "Good Condition":
                x = Inventory.objects.filter(id=id).update(i_stats="Available")

            elif remarks == "Broken":
                x = Inventory.objects.filter(id=id).update(i_stats="Broken")

            elif remarks == "Replaced":
                x = Inventory.objects.filter(id=id).update(i_stats="Replaced")

            elif remarks == "Missing some parts":
                x = Inventory.objects.filter(id=id).update(
                    i_stats="Missing some parts")

            elif remarks == "Not working":
                x = Inventory.objects.filter(
                    id=id).update(i_stats="Not working")

    messages.success(request, "Successfully done")
    return redirect('/UitcInventory')


def faculty_reqrepmain(request, id):
    a = faculty_reports.objects.get(id=id)
    print(a)
    request.POST.get('request.user.name')
    i_aor = request.POST.get("i_aor")
    ie_user = request.POST.get("ie_user")
    i_daterec2 = request.POST.get("i_daterec2")
    i_sig3 = request.POST.get("i_sig3")
    i_time2 = request.POST.get("i_time2")
    i_serv = request.POST.get("i_serv")

    if request.method == "POST":
        d = faculty_reports.objects.only('id').filter(
            fstat="Notified") | faculty_reports.objects.only('id').filter(fstat="Approved") | faculty_reports.objects.only('id').filter(fstat="On Process")
        for x in d:
            if a == x:
                faculty_reports.objects.filter(
                    id=id).update(fstat="Completed")
                faculty_reports.objects.filter(id=id).update(
                    i_aor=i_aor)
                faculty_reports.objects.filter(id=id).update(
                    i_assessby=request.user.name)
                faculty_reports.objects.filter(id=id).update(ie_user=ie_user)
                faculty_reports.objects.filter(
                    id=id).update(i_daterec2=i_daterec2)
                faculty_reports.objects.filter(id=id).update(i_sig3=i_sig3)
                faculty_reports.objects.filter(id=id).update(i_time2=i_time2)
                faculty_reports.objects.filter(id=id).update(i_serv=i_serv)

        y = faculty_reports.objects.filter(id=id).values()
        for z in y:
            name = z['fname']
            uemail = z['email3']
            print(name)
            print(uemail)
            message = "Good day " + name + \
                ", \n Your request for Repair and Maintenance has been approved, please proceed to UITC. \n UITC admin"
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


def reqrepmain_permit(request, id):
    a = faculty_reports.objects.get(id=id)
    print(a)
    request.POST.get('request.user.name')
    adm = datetime.now()
    i_dateass = request.POST.get("i_dateass")
    i_sig = request.POST.get("i_sig")
    i_dateass = request.POST.get("i_dateass")
    request.POST.get('request.user.name')
    i_quant = request.POST.get("i_quant")
    i_units = request.POST.get("i_units")
    i_partics = request.POST.get("i_partics")
    i_avail = request.POST.get("i_avail")
    i_approve = request.POST.get("i_approve")
    i_note = request.POST.get("i_note")
    request.POST.get('request.user.name')
    i_sig1 = request.POST.get("i_sig1")
    i_daterec1 = request.POST.get("i_daterec1")
    i_time1 = request.POST.get("i_time1")
    request.POST.get('request.user.name')
    i_sig2 = request.POST.get("i_sig2")
    is_date = request.POST.get("is_date")
    is_time = request.POST.get("is_time")
    ie_date = request.POST.get("ie_date")
    ie_time = request.POST.get("ie_time")
    is_rec = request.POST.get("is_rec")
    i_aor = request.POST.get("i_aor")
    ie_user = request.POST.get("ie_user")
    i_daterec2 = request.POST.get("i_daterec2")
    i_sig3 = request.POST.get("i_sig3")
    i_time2 = request.POST.get("i_time2")
    i_serv = request.POST.get("i_serv")

    if request.method == "POST":
        for x in faculty_reports.objects.only('id').filter(fstat="Notified"):
            if a == x:
                x = faculty_reports.objects.filter(
                    id=id).update(fstat="Approved")
                faculty_reports.objects.filter(id=id).update(
                    adm=adm)
                faculty_reports.objects.filter(id=id).update(
                    i_assessby=request.user.name)
                faculty_reports.objects.filter(id=id).update(i_sig=i_sig)
                faculty_reports.objects.filter(
                    id=id).update(i_dateass=i_dateass)
                faculty_reports.objects.filter(id=id).update(
                    ip_assign=request.user.name)
                faculty_reports.objects.filter(id=id).update(i_quant=i_quant)
                faculty_reports.objects.filter(id=id).update(i_units=i_units)
                faculty_reports.objects.filter(
                    id=id).update(i_partics=i_partics)
                faculty_reports.objects.filter(id=id).update(i_avail=i_avail)
                faculty_reports.objects.filter(
                    id=id).update(i_approve=i_approve)
                faculty_reports.objects.filter(id=id).update(i_note=i_note)
                faculty_reports.objects.filter(
                    id=id).update(i_coords=request.user.name)
                faculty_reports.objects.filter(id=id).update(i_sig1=i_sig1)
                faculty_reports.objects.filter(
                    id=id).update(i_daterec1=i_daterec1)
                faculty_reports.objects.filter(id=id).update(i_time1=i_time1)
                faculty_reports.objects.filter(
                    id=id).update(iu_pers=request.user.name)
                faculty_reports.objects.filter(id=id).update(i_sig2=i_sig2)
                faculty_reports.objects.filter(id=id).update(is_date=is_date)
                faculty_reports.objects.filter(id=id).update(is_time=is_time)
                faculty_reports.objects.filter(id=id).update(ie_date=ie_date)
                faculty_reports.objects.filter(id=id).update(ie_time=ie_time)
                faculty_reports.objects.filter(id=id).update(is_rec=is_rec)
                faculty_reports.objects.filter(id=id).update(i_aor=i_aor)
                faculty_reports.objects.filter(id=id).update(ie_user=ie_user)
                faculty_reports.objects.filter(
                    id=id).update(i_daterec2=i_daterec2)
                faculty_reports.objects.filter(id=id).update(i_sig3=i_sig3)
                faculty_reports.objects.filter(id=id).update(i_time2=i_time2)
                faculty_reports.objects.filter(id=id).update(i_serv=i_serv)

        y = faculty_reports.objects.filter(id=id).values()
        for z in y:
            name = z['fname']
            uemail = z['email3']
            print(name)
            print(uemail)
            message = "Good day " + name + \
                ", \n Your request for Repair and Maintenance has been approved, please fill up the and sign the form in your report. \n UITC admin"
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


def reqrepmain_cancel(request, id):
    if request.method == 'POST':
        a = faculty_reports.objects.get(id=id)
        reason = request.POST.get("reasonrp")
        for x in faculty_reports.objects.only('id').filter(fstat="On process"):
            if a == x:
                x = faculty_reports.objects.filter(
                    id=id).update(fstat="Declined")
                y = faculty_reports.objects.filter(id=id).values()
                for z in y:
                    name = z['fname']
                    uemail = z['email3']
                    print(name)
                    print(uemail)
                print(reason)
                message = "Good day " + name + \
                    ", \n Your request for repair and maintence has been declined, " + \
                    reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Completed")
    return redirect('/UitcReports')


def notify_rp(request, id):
    if request.method == 'POST':
        a = faculty_reports.objects.get(id=id)
        reason = request.POST.get("message")
        asd = faculty_reports.objects.only('id').filter(
            fstat="On process") | faculty_reports.objects.only('id').filter(fstat="Notified")
        for x in asd:
            if a == x:
                x = faculty_reports.objects.filter(
                    id=id).update(fstat="Notified")
                y = faculty_reports.objects.filter(id=id).values()
                for z in y:
                    name = z['fname']
                    uemail = z['email3']
                    print(name)
                    print(uemail)
                print(reason)
                message = "Good day " + name + ", " + reason + "\n UITC admin"
                email = EmailMessage(
                    name,
                    message,
                    'tupc.uitconlinesystem@gmail.com',
                    [uemail],

                )

                email.send()
                break
    messages.info(request, "Completed")
    return redirect('/UitcReports')

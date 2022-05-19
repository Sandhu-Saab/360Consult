from django.shortcuts import render, redirect
from .models import Contect_us
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def homepage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        contectokk = Contect_us(name=name, email=email, phone=phone, msg=msg)
        sub = "Received New Message from Client"
        message = "Hello " + name + " has filled your form. Kindly contact him/her on " + phone + "\nMessage from " + name + " is\n " + msg
        emailFrom = settings.EMAIL_HOST_USER
        # htmlMes = "<div style='background-color: #601410;'><h2>Hello</h2>  <span> new message received </span></div>"
        recip = ["sharandeep.sandhu29@gmail.com"]
        send_mail(subject=sub, message=message, from_email=emailFrom, recipient_list=recip)
        # send_mail(subject=sub, message=message, from_email=emailFrom, recipient_list=recip, html_message=htmlMes)
        print("sffgfdgfddfsdfsdfsdfsdfd", contectokk)
        contectokk.save()
    return render(request, "index.html")


def okk(request):
    return render(request, "okk.html")


def service(request):
    return render(request, "service.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        contectokk = Contect_us(name=name, email=email, phone=phone, msg=msg)
        sub = "Received New Message from Client"
        message = "Hello " + name + " has filled your form. Kindly contact him/her on " + phone + "\nMessage from " + name + " is\n " + msg
        emailFrom = settings.EMAIL_HOST_USER
        # htmlMes = "<div style='background-color: #601410;'><h2>Hello</h2>  <span> new message received </span></div>"
        recip = ["sharandeep.sandhu29@gmail.com"]
        send_mail(subject=sub, message=message, from_email=emailFrom, recipient_list=recip)
        # send_mail(subject=sub, message=message, from_email=emailFrom, recipient_list=recip, html_message=htmlMes)
        print("sffgfdgfddfsdfsdfsdfsdfd", contectokk)
        contectokk.save()
    return render(request, "contact.html")

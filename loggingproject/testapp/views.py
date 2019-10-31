from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

#send_mail(subject,message,from mail,to mail)
import logging


def index(request):
    send_mail("hello",'I love U','fbtest1206@gmail.com',['harikareddymenakuri@gmail.com','harikanth225@gmail.com'])
    # try:
    #     logging.getLogger('error_logger').error("Hi i am here")
    #     msg = 1/0
    # except Exception as e:
    #     logging.getLogger('error_logger').exception(e)
    return HttpResponse("This is first logging application")

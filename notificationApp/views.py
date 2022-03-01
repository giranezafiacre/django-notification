from django.shortcuts import render
from notificationApp.send_mail import send_mail

from notificationApp.send_sms import send_sms
from rest_framework import response,status
from rest_framework.decorators import api_view
# Create your views here.
# API
@api_view(['POST'])
def send_sms_view(request):
    print(request.POST['receiver'])
    json_result=send_sms(request.POST['receiver'])
    return response.Response(data=json_result, status=status.HTTP_200_OK)

@api_view(['POST'])
def send_email_view(request):
    print(request.POST['receiver'])
    json_result=send_mail(request.POST['receiver'])
    return response.Response(data=json_result, status=status.HTTP_200_OK)
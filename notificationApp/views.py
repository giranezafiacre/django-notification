from django.http import HttpResponseRedirect
from django.shortcuts import render
from notificationApp.forms import emailForm, phoneForm
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

def send_sms_view1(request):
    if request.method == 'POST':
        form = emailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            json_result=send_sms(request.POST['receiver'])
            print(json_result)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = phoneForm()

    return render(request, 'send_email.html', {'form': form})

def send_email_view1(request):
    if request.method == 'POST':
        form = emailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            json_result=send_mail(request.POST['receiver'])
            print(json_result)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = emailForm()

    return render(request, 'send_email.html', {'form': form})
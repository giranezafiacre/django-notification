from django.urls import path
from . import views

urlpatterns = [
   path('send_sms/', views.send_sms_view, name='sms-api'),
   path('send_mail/', views.send_email_view, name='email-api'),
   path('send_sms1/', views.send_sms_view1, name='sms'),
   path('send_mail1/', views.send_email_view1, name='email'),
]

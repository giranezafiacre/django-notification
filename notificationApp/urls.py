from django.urls import path
from . import views

urlpatterns = [
   path('send_sms/', views.send_sms_view, name='sms-api'),
   path('send_mail/', views.send_email_view, name='email-api'),
]

from django import forms

# creating a form
class emailForm(forms.Form):
    receiver = forms.CharField(label='receiver email', max_length=100)

		
class phoneForm(forms.Form):
    receiver = forms.CharField(label='receiver phone', max_length=100)
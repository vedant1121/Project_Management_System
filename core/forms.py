from django import forms
from .models import Contactus
# from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=50)
    contactno = forms.CharField(max_length=12)
    message = forms.CharField(max_length=200)


    def save(self, commit=True):
        con = Contactus()
        con.name = self.cleaned_data['name']
        con.email = self.cleaned_data['email']
        con.contactno = self.cleaned_data['contactno']
        con.message = self.cleaned_data['message']

        if commit:
            con.save()


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'app-form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['class'] = 'app-form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['contactno'].widget.attrs['class'] = 'app-form-control'
        self.fields['contactno'].widget.attrs['placeholder'] = 'Contact No.'
        self.fields['message'].widget.attrs['class'] = 'app-form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter Message'
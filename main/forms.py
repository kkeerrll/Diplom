from django import forms

# class PhoneNumber(forms.Form):
#     phone_number = forms.CharField(label = 'Номер')

from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()

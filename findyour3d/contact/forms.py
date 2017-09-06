from django import forms
from django.core.mail import EmailMessage

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'subject', 'body')

# class ContactForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     body = forms.CharField()
#
#
#     def save(self):
#         contact = Contact(
#             first_name=self.cleaned_data['name'],
#             email=self.cleaned_data['email'],
#             body=self.cleaned_data['body']
#         )
#         cont = contact.save()
#
#         body = 'From: {}\n Name: {}\n Body: {}'.format(self.cleaned_data['email1'],
#                                                        self.cleaned_data['first_name'],
#                                                        self.cleaned_data['body'])
#
#         email = EmailMessage(
#             'Contact Form',
#             body,
#             self.cleaned_data['email'],
#             ['adubnyak@gmail.com', ],
#             ['adubnyak@gmail.com', ],
#             reply_to=['adubnyak@gmail.com'],
#         )
#
#         email.send()
#         return cont

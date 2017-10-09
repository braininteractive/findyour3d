from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'subject', 'body')

        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'})
        }

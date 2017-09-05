from django import forms
from .models import Customer


class AddCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['prototype_type', 'need_assistance', 'basic_material', 'material', 'process',
                  'is_flexible', 'is_semi_biodegradable', 'is_heat_withstand', 'size',
                  'consideration', 'budget', 'geo_matters', 'description', 'cad_file', 'user', 'state']

        widgets = {
            'prototype_type': forms.Select(attrs={'class': 'form-control edited'}),
            'need_assistance': forms.Select(attrs={'class': 'form-control edited'}),
            # 'basic_material': forms.Select(attrs={'class': 'form-control edited'}),
            'material': forms.Select(attrs={'class': 'form-control edited'}),
            'process': forms.Select(attrs={'class': 'form-control edited'}),
            'size': forms.Select(attrs={'class': 'form-control edited'}),
            'consideration': forms.Select(attrs={'class': 'form-control edited'}),
            'budget': forms.Select(attrs={'class': 'form-control edited'}),
            'geo_matters': forms.Select(attrs={'class': 'form-control edited'}),
            'state': forms.Select(attrs={'class': 'form-control edited'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cad_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'basic_material': forms.RadioSelect(attrs={'id': 'a_value', 'class': 'md-radiobtn'}),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = None
        if 'user' in kwargs['initial']:
            self.user = kwargs['initial'].pop('user')

        super(AddCustomerForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.user

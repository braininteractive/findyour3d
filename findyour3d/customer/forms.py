from django import forms
from .models import Customer


class AddCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['prototype_type', 'need_assistance', 'basic_material', 'material', 'process',
                  'is_flexible', 'is_semi_biodegradable', 'is_heat_withstand', 'size',
                  'consideration', 'budget', 'geo_matters', 'description', 'cad_file']

        widgets = {
            'prototype_type': forms.Select(attrs={'class': 'form-control'}),
            'need_assistance': forms.Select(attrs={'class': 'form-control'}),
            'basic_material': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'process': forms.Select(attrs={'class': 'form-control'}),
            # 'is_flexible': forms.Select(attrs={'class': 'form-control'}),
            # 'is_semi_biodegradable': forms.Select(attrs={'class': 'form-control'}),
            # 'is_heat_withstand': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'consideration': forms.Select(attrs={'class': 'form-control'}),
            'budget': forms.Select(attrs={'class': 'form-control'}),
            'geo_matters': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cad_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddCustomerForm, self).__init__(*args, **kwargs)

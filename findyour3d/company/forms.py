from django import forms
from .models import Company


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'display_name', 'address_line_1', 'address_line_2',
                  'full_name', 'email', 'phone', 'website', 'ideal_customer',
                  'is_cad_assistance', 'budget', 'basic_material', 'consideration',
                  'printing_options', 'material', 'top_printing_processes',
                  'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'ideal_customer': forms.Select(attrs={'class': 'form-control'}),
            'budget': forms.Select(attrs={'class': 'form-control'}),
            'basic_material': forms.Select(attrs={'class': 'form-control'}),
            'consideration': forms.Select(attrs={'class': 'form-control'}),
            'printing_options': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'top_printing_processes': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(AddCompanyForm, self).__init__(*args, **kwargs)

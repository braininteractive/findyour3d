from django import forms
from .models import Company


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'display_name', 'address_line_1', 'address_line_2',
                  'full_name', 'email', 'phone', 'website', 'ideal_customer',
                  'is_cad_assistance', 'budget',
                  'printing_options', 'material', 'top_printing_processes',
                  'description', 'user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'ideal_customer': forms.Select(attrs={'class': 'form-control edited'}),
            'budget': forms.Select(attrs={'class': 'form-control edited'}),
            # 'basic_material': forms.Select(attrs={'class': 'form-control edited'}),
            # 'consideration': forms.Select(attrs={'class': 'form-control edited'}),
            'printing_options': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'material': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'top_printing_processes': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = None
        if 'user' in kwargs['initial']:
            self.user = kwargs['initial'].pop('user')

        super(AddCompanyForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.user
        self.fields['ideal_customer'].label = 'What is your company’s ideal customer that we should send to you?'
        self.fields['budget'].label = 'What is your ideal order cost/budget?'
        self.fields['printing_options'].label = 'Printing Options Available'


class EditCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'display_name', 'logo', 'address_line_1', 'address_line_2',
                  'full_name', 'email', 'phone', 'website', 'ideal_customer',
                  'is_cad_assistance', 'budget',
                  'printing_options', 'material', 'top_printing_processes',
                  'description', 'user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'ideal_customer': forms.Select(attrs={'class': 'form-control edited'}),
            'budget': forms.Select(attrs={'class': 'form-control edited'}),
            'printing_options': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'material': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'top_printing_processes': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = None
        if 'user' in kwargs['initial']:
            self.user = kwargs['initial'].pop('user')

        super(EditCompanyForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.user
        self.fields['ideal_customer'].label = 'What is your company’s ideal customer that we should send to you?'
        self.fields['budget'].label = 'What is your ideal order cost/budget?'
        self.fields['printing_options'].label = 'Printing Options Available'

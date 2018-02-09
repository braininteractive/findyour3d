from django import forms

from .models import Company, SpecialOffer


EXPEDITED_CHOICES = (
    (0, 'No, we do not offer any expedited shipping options.'),
    (1, 'Yes we offer an expedited process for a fee.')
)


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
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
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
        self.fields['printing_options'].label = 'Printing Processes Available'


class EditCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'display_name', 'logo', 'address_line_1', 'address_line_2',
                  'full_name', 'email', 'phone', 'website', 'ideal_customer',
                  'is_cad_assistance', 'budget',
                  'printing_options', 'material', 'top_printing_processes',
                  'description', 'user', 'is_expedited', 'shipping']

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
            'is_expedited': forms.Select(attrs={'class': 'form-control edited'}, choices=EXPEDITED_CHOICES),
            'printing_options': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'material': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'top_printing_processes': forms.SelectMultiple(attrs={'class': 'form-control edited'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'shipping': forms.Select(attrs={'class': 'form-control edited'}),
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
        self.fields['is_expedited'].label = 'Do you offer an expedited manufacturing process?'
        self.fields['shipping'].label = 'Which of the following shipping options do you offer?'


class AddSpecialOfferForm(forms.ModelForm):

    class Meta:
        model = SpecialOffer
        fields = ('text', 'company')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                                          'placeholder': 'eg: 25% off for next order!'}),
            'company': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        self.user = None
        if 'company' in kwargs['initial']:
            self.company = kwargs['initial'].pop('company')

        super(AddSpecialOfferForm, self).__init__(*args, **kwargs)
        self.fields['company'].initial = self.company

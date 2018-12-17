from django import forms
from django.core.exceptions import ValidationError

from .models import Customer

TIME_CHOICES = (
    (0, 'No, timing is not an issue for me.'),
    (1, 'Yes, I need this project manufactured as soon as physically possible.')
)


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['prototype_type', 'customer_type', 'need_assistance', 'material', 'process',
                  'size', 'is_expedited', 'shipping',
                  'budget', 'description', 'cad_file', 'user']

        widgets = {
            'prototype_type': forms.RadioSelect(attrs={'id': 'a_value', 'class': 'md-radiobtn'}),
            'budget': forms.RadioSelect(attrs={'id': 'b_value', 'class': 'md-radiobtn'}),
            'customer_type': forms.RadioSelect(attrs={'id': 'c_value', 'class': 'md-radiobtn'}),
            'material': forms.Select(attrs={'class': 'form-control edited', 'style': 'margin-top: 15px'}),
            'process': forms.Select(attrs={'class': 'form-control edited', 'style': 'margin-top: 15px'}),
            'size': forms.RadioSelect(attrs={'id': 'd_value', 'class': 'md-radiobtn'}),
            'need_assistance': forms.RadioSelect(attrs={'id': 'e_value', 'class': 'md-radiobtn'}),
            'is_expedited': forms.RadioSelect(attrs={'id': 'h_value', 'class': 'md-radiobtn'}),
            'shipping': forms.RadioSelect(attrs={'id': 'g_value', 'class': 'md-radiobtn'}),
            'geo_matters': forms.Select(attrs={'class': 'form-control edited'}),
            'zip': forms.TextInput(attrs={'class': 'form-control edited'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-20', 'rows': 10}),
            'cad_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),

            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = None
        if 'user' in kwargs['initial']:
            self.user = kwargs['initial'].pop('user')

        super(AddCustomerForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.user
        self.fields['prototype_type'].label = 'Is this a single "Prototype" run or multiple unit batch?'
        self.fields['budget'].label = 'Roughly what is your overall budget for this project?'
        self.fields['customer_type'].label = 'What would you classify yourself as?'
        self.fields['material'].label = 'If you know the exact Material you wish to use, enter it here.'
        self.fields['process'].label = 'If You Know The Exact Printing Process You Want, Select It Here.'
        self.fields['size'].label = 'Roughly what will be the size of your design?'
        self.fields['need_assistance'].label = 'Will you need assistance rendering a 3D CAD model for printing?'
        self.fields['is_expedited'].label = 'Do you require expedited manufacturing for your project? ' \
                                            '(Note, a rapid manufacturing process may add cost to your project)'
        self.fields['shipping'].label = 'Do you require any of the following shipping options for your project? ' \
                                        '(Note, additional shipping may cost extra)'
        self.fields['description'].label = 'Please write a description of your project and any additional ' \
                                           'comments you would like your service provider to know.'
        self.fields['cad_file'].label = 'If you have a CAD File for your project, please upload it here. '
        self.fields['is_expedited'].required = True
        self.fields['shipping'].required = False


class AddAdvancedCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['basic_material', 'is_precious_metal', 'metal_concern', 'metal_decision',
                  'other_materials',
                  'plastic_concern', 'is_food_safe_plastic', 'is_functional_or_basic',
                  'plastic_decision', 'heat_resistance', 'is_extreme_strength', 'is_better_appearance',
                  'is_highest_detail', 'is_full_color', 'is_able_to_bend', 'performance_or_price']

        widgets = {
            'basic_material': forms.Select(attrs={'class': 'form-control edited'}),
            'is_precious_metal': forms.Select(attrs={'class': 'form-control edited'}),
            'is_food_safe_plastic': forms.Select(attrs={'class': 'form-control edited'}),
            'is_extreme_strength': forms.Select(attrs={'class': 'form-control edited'}),
            'is_better_appearance': forms.Select(attrs={'class': 'form-control edited'}),
            'is_highest_detail': forms.Select(attrs={'class': 'form-control edited'}),
            'is_full_color': forms.Select(attrs={'class': 'form-control edited'}),
            'is_able_to_bend': forms.Select(attrs={'class': 'form-control edited'}),
            'performance_or_price': forms.Select(attrs={'class': 'form-control edited'}),

        }

    def __init__(self, *args, **kwargs):

        super(AddAdvancedCustomerForm, self).__init__(*args, **kwargs)

        self.fields['basic_material'].label = 'Select your basic Material type'
        self.fields['is_precious_metal'].label = 'Do you want your project to be constructed by functional metals ' \
                                                 'or precious metals, such as silver or gold?'
        self.fields['metal_concern'].label = 'Which is your chief concern? Conductivity or pure Strength'
        self.fields['metal_decision'].label = 'Are you willing to spend top dollar for the best strength and ' \
                                              'resistance available? (Industrial Grade)'
        self.fields['other_materials'].label = 'Are you looking for a Wood-like print or a Stone print for your ' \
                                               'project?'
        self.fields['plastic_concern'].label = 'What is more important your project, cost or quality of the print?'
        self.fields['is_food_safe_plastic'].label = 'Do you wish your project to be food-safe?'
        self.fields['is_functional_or_basic'].label = 'Do you need your project to be functional or just printed as ' \
                                                      'basic as possible?'
        self.fields['plastic_decision'].label = 'Would you pay slightly higher prices for slightly more ' \
                                                'strength and flexibility?'
        self.fields['heat_resistance'].label = 'Does your project require Flexibility or Heat Resistance?'
        self.fields['is_extreme_strength'].label = 'Are you willing to spend top dollar for extreme performance ' \
                                                   'and strength?'
        self.fields['is_better_appearance'].label = 'Do you want your project to have a better appearance ' \
                                                    'or functionality?'
        self.fields['is_highest_detail'].label = 'Are you looking for the best details possible for small and ' \
                                                 'intricate designs for a premium cost?'
        self.fields['is_full_color'].label = 'Will Your project require rich and full color?'
        self.fields['is_able_to_bend'].label = 'Do you want your project to be able to bend under some ' \
                                               'pressure or act similar to rubber?'
        self.fields['performance_or_price'].label = 'Would you settle for slightly less performance for slightly' \
                                                    'less price?'

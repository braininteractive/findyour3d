from django import forms
from .models import Customer

METAL_DECISION_CHOICES = (
    (1, 'Unknown'),
    (2, 'I want the very best for top dollar. ($250+ per print)'),
    (3, 'No, but I still want a high quality metal')
)

IS_FOOD_SAFE_CHOICES = (
    (1, 'Unknown'),
    (2, 'I want my project to be generally safe around food'),
    (3, "No, I don't need my project to be foodsafe")
)

EXTREME_CHOICES = (
    (1, 'Unknown'),
    (2, 'I am willing to spend top dollar ($250+) for the very best quality available'),
    (3, "No I don't need extreme strength and performance")
)

APPEARANCE_CHOICES = (
    (1, 'Unknown'),
    (2, 'I want a more functional material for my project'),
    (3, 'I want a better looking appearance for my project')
)

BEST_DETAILS_CHOICES = (
    (1, 'Unknown'),
    (2, 'Yes, I want the highest detail possible'),
    (3, "I want detail, but don't need the highest detail possible")
)

COLORS_CHOICES = (
    (1, 'Unknown'),
    (2, 'Yes, I want rich and full colors for my project'),
    (3, "No I don't need my project to have full colors, just printed in high detail")
)

BEND_CHOICES = (
    (1, 'Unknown'),
    (2, 'I want my project to handle some bending, but not to be rubber like'),
    (3, "I want my project to feel and act almost like rubber")
)


class AddCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['basic_material', 'is_precious_metal', 'metal_concern', 'metal_decision',
                  'other_materials',
                  'plastic_concern', 'is_food_safe_plastic', 'is_functional_or_basic',
                  'plastic_decision', 'heat_resistance', 'is_extreme_strength', 'is_better_appearance',
                  'is_highest_detail', 'is_full_color', 'is_able_to_bend',
                  'prototype_type', 'need_assistance', 'material', 'process',
                  'is_flexible', 'is_semi_biodegradable', 'is_heat_withstand', 'size',
                  'consideration', 'budget', 'geo_matters', 'description', 'cad_file', 'user', 'state']

        widgets = {
            'prototype_type': forms.Select(attrs={'class': 'form-control edited'}),
            'need_assistance': forms.Select(attrs={'class': 'form-control edited'}),
            'material': forms.Select(attrs={'class': 'form-control edited'}),
            'process': forms.Select(attrs={'class': 'form-control edited'}),
            'size': forms.Select(attrs={'class': 'form-control edited'}),
            'consideration': forms.Select(attrs={'class': 'form-control edited'}),
            'budget': forms.Select(attrs={'class': 'form-control edited'}),
            'geo_matters': forms.Select(attrs={'class': 'form-control edited'}),
            'state': forms.Select(attrs={'class': 'form-control edited'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cad_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),

            # 'basic_material': forms.RadioSelect(attrs={'id': 'a_value', 'class': 'md-radiobtn'}),
            'basic_material': forms.Select(attrs={'class': 'form-control edited'}),

            'is_precious_metal': forms.Select(attrs={'class': 'form-control edited'},
                                              choices=METAL_DECISION_CHOICES),
            'is_food_safe_plastic': forms.Select(attrs={'class': 'form-control edited'},
                                                 choices=IS_FOOD_SAFE_CHOICES),
            'is_extreme_strength': forms.Select(attrs={'class': 'form-control edited'},
                                                choices=EXTREME_CHOICES),
            'is_better_appearance': forms.Select(attrs={'class': 'form-control edited'},
                                                 choices=APPEARANCE_CHOICES),
            'is_highest_detail': forms.Select(attrs={'class': 'form-control edited'},
                                              choices=BEST_DETAILS_CHOICES),
            'is_full_color': forms.Select(attrs={'class': 'form-control edited'},
                                          choices=COLORS_CHOICES),
            'is_able_to_bend': forms.Select(attrs={'class': 'form-control edited'},
                                            choices=BEND_CHOICES),


            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = None
        if 'user' in kwargs['initial']:
            self.user = kwargs['initial'].pop('user')

        super(AddCustomerForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.user
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


from django.db import models
from django.conf import settings
from findyour3d.utils.models import (BASIC_MATERIAL_CHOICES, BUDGET_CHOICES, CONSIDERATION_CHOICES,
                                     MATERIAL_CHOICES)


PROTOTYPES_CHOICES = (
    (0, 'Single Unit'),
    (1, 'Multiple Units'),
)

ASSISTANCE_CHOICES = (
    (0, 'No, I have my own 3D CAD model ready to upload.'),
    (1, 'Yes, I need help designing a 3D model.'),
)

PROCESS_CHOICES = (
    (0, 'Fused Deposition Modeling (FDM)'),
    (1, 'Stereoligtography (SLM)'),
    (2, 'Selective Laser Sintering (SLS)'),
    (3, 'Material Jetting (MJ)'),
    (4, 'Binder Jetting (BJ) (Stone)'),
    (5, 'Electron Beam Melting (EBM) (Metals)'),
)

SIZES_CHOICES = (
    (0, 'I am not sure'),
    (1, 'Small (Cubic Millimeters)'),
    (2, 'Medium (Cubic Centimeters)'),
    (3, 'Large (Cubic Meters)'),
)

GEO_MATTERS_CHOICES = (
    (0, 'No, I do not care about location.'),
    (1, 'Yes, I want to be close to my provider.'),
)

STATES_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

METAL_CONCERN_CHOICES = (
    (0, 'None'),
    (1, 'Conductivity'),
    (2, 'Strength')
)

PLASTIC_CONCERN_CHOICES = (
    (0, 'None'),
    (1, 'My chief concern is cost'),
    (2, 'My chief concern is quality of the print')
)

METAL_DECISION_CHOICES = (
    (0, 'None'),
    (1, 'I want the very best for top dollar. ($250+ per print)'),
    (2, 'No, but I still want a high quality metal')
)

OTHER_DECISION_CHOICES = (
    (0, 'None'),
    (1, 'I want my project to be wood-like'),
    (2, 'I want my project to be made from stone')
)

IF_FOOD_SAFE_CHOICES = (
    (0, 'None'),
    (1, 'Yes, I want my project to be as functional as possible for the cost'),
    (2, 'No, I just need my projected to be printed very simply')
)

IF_NOT_FOOD_SAFE_CHOICES = (
    (0, 'None'),
    (1, 'Higher Prices'),
    (2, 'As Basic as possible')
)
PLASTIC_DECISION_CHOICES = (
    (0, 'None'),
    (1, 'Yes, I am willing to pay slightly more to get a better material'),
    (2, 'No I want my project to pretty simple for a pretty low price')
)
HEAT_RESISTANCE_CHOICES = (
    (0, 'None'),
    (1, 'I want my project to be able to withstand heat.'),
    (2, 'My project requires neither heat resistance or flexibility'),
    (3, 'I want my project to be flexible'),
)

CUSTOMER_TYPE_CHOICES = (
    (0, 'Individual'),
    (1, 'A Small Business'),
    (2, 'Industrial Business')
)

SHIPPING_CHOICES = (
    (0, 'No, timing is not an issue for me.'),
    (1, 'Yes, I need this project manufactured as soon as physically possible.')
)


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    prototype_type = models.IntegerField(choices=PROTOTYPES_CHOICES, default=0)
    budget = models.IntegerField(choices=BUDGET_CHOICES, default=0)
    customer_type = models.IntegerField(choices=CUSTOMER_TYPE_CHOICES, default=0)
    material = models.IntegerField(choices=MATERIAL_CHOICES, blank=True, null=True)
    process = models.IntegerField(choices=PROCESS_CHOICES, blank=True, null=True)
    size = models.IntegerField(choices=SIZES_CHOICES, default=0)
    need_assistance = models.IntegerField(choices=ASSISTANCE_CHOICES, default=0)
    is_time_sensitive = models.BooleanField(default=False)
    shipping = models.IntegerField(choices=SHIPPING_CHOICES, default=0)
    geo_matters = models.IntegerField(choices=GEO_MATTERS_CHOICES, default=0)
    zip = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    cad_file = models.FileField(upload_to='cads/', blank=True, null=True)

    basic_material = models.IntegerField(choices=BASIC_MATERIAL_CHOICES, default=0)

    # METALS
    is_precious_metal = models.NullBooleanField()
    # if NOT is_precious_metal:
    metal_concern = models.IntegerField(choices=METAL_CONCERN_CHOICES, default=0)
    metal_decision = models.IntegerField(choices=METAL_DECISION_CHOICES, default=0)

    # OTHER
    other_materials = models.IntegerField(choices=OTHER_DECISION_CHOICES, default=0)

    # PLASTIC/RESINS
    plastic_concern = models.IntegerField(choices=PLASTIC_CONCERN_CHOICES, default=0)

    # if Cost:
    is_food_safe_plastic = models.NullBooleanField()
    # if is_food_safe_plastic:
    is_functional_or_basic = models.IntegerField(choices=IF_FOOD_SAFE_CHOICES, default=0)
    # if NOT is_food_safe_plastic:
    plastic_decision = models.IntegerField(choices=PLASTIC_DECISION_CHOICES, default=0)

    # if Quality:
    heat_resistance = models.IntegerField(choices=HEAT_RESISTANCE_CHOICES, default=0)
    # if Heat:
    is_extreme_strength = models.NullBooleanField()
    # if NOT is_extreme_strength:
    is_better_appearance = models.NullBooleanField()

    # if neither:
    is_highest_detail = models.NullBooleanField()
    # if is_highest_detail:
    is_full_color = models.NullBooleanField()

    # if flexible:
    is_able_to_bend = models.NullBooleanField()

    # NOT IN USE
    is_flexible = models.BooleanField(default=True)
    is_semi_biodegradable = models.BooleanField(default=True)
    is_heat_withstand = models.BooleanField(default=True)
    consideration = models.IntegerField(choices=CONSIDERATION_CHOICES, default=0)
    state = models.CharField(max_length=3, choices=STATES_CHOICES, blank=True, null=True)
    is_advanced_filled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "%s" % self.user

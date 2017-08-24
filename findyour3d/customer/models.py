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
    ('KS', 'Kansas)'),
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


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    prototype_type = models.IntegerField(choices=PROTOTYPES_CHOICES, default=0)
    need_assistance = models.IntegerField(choices=ASSISTANCE_CHOICES, default=0)
    basic_material = models.IntegerField(choices=BASIC_MATERIAL_CHOICES, default=0)
    material = models.IntegerField(choices=MATERIAL_CHOICES, blank=True, null=True)
    process = models.IntegerField(choices=PROCESS_CHOICES, blank=True, null=True)
    is_flexible = models.BooleanField(default=True)
    is_semi_biodegradable = models.BooleanField(default=True)
    is_heat_withstand = models.BooleanField(default=True)
    size = models.IntegerField(choices=SIZES_CHOICES, default=0)
    consideration = models.IntegerField(choices=CONSIDERATION_CHOICES, default=0)
    budget = models.IntegerField(choices=BUDGET_CHOICES, default=0)
    geo_matters = models.IntegerField(choices=GEO_MATTERS_CHOICES, default=0)
    state = models.CharField(max_length=3, choices=STATES_CHOICES, blank=True, null=True)
    description = models.TextField()
    cad_file = models.FileField(upload_to='cads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "%s" % self.user

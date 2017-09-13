from django.db import models
from django.conf import settings

from multiselectfield import MultiSelectField

from findyour3d.utils.models import (BASIC_MATERIAL_CHOICES, BUDGET_CHOICES, CONSIDERATION_CHOICES,
                                     MATERIAL_CHOICES)

CUSTOMER_CHOICES = (
    (0, 'Individuals'),
    (1, 'Small Businesses'),
    (2, 'Large/Industrial Businesses'),
)

PRINTING_OPTIONS_CHOICES = (
    (0, 'FDM (Fused Deposition Modeling)'),
    (1, 'SLA (Sterolithography)'),
    (2, 'DLP (Digital Light Processing)'),
    (3, 'SLS (Selective Laser Sintering)'),
    (4, 'Material Jetting (PolyJet / MultiJet)'),
    (5, 'BJ (Binderjetting)'),
    (6, 'EBM (Electron Beam Melting)'),
)


class Company(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    ideal_customer = models.IntegerField(choices=CUSTOMER_CHOICES, default=0)
    is_cad_assistance = models.BooleanField(default=False)
    budget = models.IntegerField(choices=BUDGET_CHOICES, default=0)
    basic_material = models.IntegerField(choices=BASIC_MATERIAL_CHOICES, default=0)
    consideration = models.IntegerField(choices=CONSIDERATION_CHOICES, default=0)
    printing_options = MultiSelectField(choices=PRINTING_OPTIONS_CHOICES)
    material = models.IntegerField(choices=MATERIAL_CHOICES, blank=True, null=True)
    top_printing_processes = MultiSelectField(choices=PRINTING_OPTIONS_CHOICES, max_choices=3)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name_plural = 'Companies'


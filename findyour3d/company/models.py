from django.db import models
from django.conf import settings

from multiselectfield import MultiSelectField
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

from findyour3d.customer.models import (BASIC_MATERIAL_CHOICES, BUDGET_CHOICES, CONSIDERATION_CHOICES,
                                        MATERIAL_CHOICES, PROCESS_CHOICES, SHIPPING_CHOICES)

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


class CompanyManager(models.Manager):

    def active(self):
        return self.filter(quote_limit__gt=0).order_by('-user__plan')


class Company(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    ideal_customer = MultiSelectField(choices=CUSTOMER_CHOICES, default=0)
    is_cad_assistance = models.BooleanField(default=False)
    budget = MultiSelectField(choices=BUDGET_CHOICES, default=0)
    basic_material = models.IntegerField(choices=BASIC_MATERIAL_CHOICES, default=0)
    consideration = models.IntegerField(choices=CONSIDERATION_CHOICES, default=0)
    printing_options = MultiSelectField(choices=PRINTING_OPTIONS_CHOICES)
    material = MultiSelectField(choices=MATERIAL_CHOICES, blank=True, null=True)
    top_printing_processes = MultiSelectField(choices=PROCESS_CHOICES, max_choices=9)
    description = models.TextField()
    ratings = GenericRelation(Rating)
    is_expedited = models.BooleanField(default=True)
    shipping = MultiSelectField(choices=SHIPPING_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quote_limit = models.IntegerField(default=10)

    objects = CompanyManager()

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name_plural = 'Companies'

    def get_rating(self):
        return int(self.ratings.ratings_for_instance(self).average)

    def get_rating_html_snippet(self):
        rating = self.get_rating()
        gold_star = '<i class="fa fa-star yellow-600"></i>'
        gray_star = gold_star.replace(' yellow-600', '')
        html = gray_star * 5
        if rating:
            if rating < 5:
                additional_stars = 5 - rating
                html = (gold_star * rating) + (additional_stars * gray_star)
            elif rating == 5:
                html = rating * gold_star
        else:
            html = gray_star * 5
        return html

    def get_quote_limit(self):
        if self.quote_limit <= 3:
            return '<span style="color: red">{}</span>'.format(self.quote_limit)
        else:
            return self.quote_limit

    def get_is_cad_assistance_snippet(self):
        if self.is_cad_assistance:
            sign = 'check'
        else:
            sign= 'times'
        snippet = '<i class="fa fa-{} grey-600"></i>'.format(sign)
        return snippet


class SpecialOffer(models.Model):
    company = models.ForeignKey('Company')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.company

import random
import string

import jsonfield
from django.core.validators import MaxValueValidator

from django.db import models
from django.conf import settings
from decimal import Decimal


PAYMENT_STATUS = (
    ('1', 'Failed'),
    ('2', 'Success'),
    ('3', 'Pending'),
)


class UserPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    trx_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.CharField(max_length=255, blank=True, null=True)
    recipient_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    transferred = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default='1')
    history = jsonfield.JSONField(
        default={},
        verbose_name="Response",
        help_text="JSON containing response Card from stripe"
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __unicode__(self):
        return "%s's payment" % self.user


class Coupon(models.Model):
    number = models.CharField(max_length=6, unique=True, blank=True, null=True,
                              help_text='Leave blank if you want coupon number to be generated automatically')
    duration = models.IntegerField(blank=True, null=True,
                                   help_text='Coupon duration in days. Leave blank if its a one-time deal')
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100), ],
                                           help_text='Discount value in percents, for e.g. 10 or 50')
    expired = models.BooleanField(default=False)
    activated_at = models.DateTimeField(blank=True, null=True)
    activated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    @staticmethod
    def coupon_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = self.coupon_generator()
            while Coupon.objects.filter(number=self.number).exists():
                self.number = self.coupon_generator()
        super(Coupon, self).save()

    def __unicode__(self):
        return str(self.number)

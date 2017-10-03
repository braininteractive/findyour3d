import jsonfield

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


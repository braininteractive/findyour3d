from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    TYPE_CHOICES = (
        (1, 'Customer'),
        (2, 'Company')
    )

    PLAN_CHOICES = (
        (1, 'Starter'),
        (2, 'Premium')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    user_type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    default_card = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name='Default Card ID')
    card_last = models.CharField(max_length=255, blank=True, null=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    card_expiry = models.CharField(blank=True, null=True, max_length=255)
    payment_active = models.BooleanField(default=False)
    payment_issue = models.CharField(max_length=255, blank=True, null=True)

    plan = models.IntegerField(choices=PLAN_CHOICES, blank=True, null=True)

    is_trial = models.BooleanField(default=True)
    is_cancelled = models.BooleanField(default=False)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

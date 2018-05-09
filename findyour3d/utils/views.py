import urllib
import calendar
import datetime
from django.utils import timezone
from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from findyour3d.payment.models import Coupon


def custom_redirect(url_name, *args, **kwargs):
    url = reverse(url_name, args=args)
    params = urllib.parse.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)


def add_months(source_date, months):
    month = source_date.month - 1 + months
    year = int(source_date.year + month / 12)
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def get_amount_with_discount(user, amount):
    if Coupon.objects.filter(activated_by=user).exists():
        coupon = Coupon.objects.get(activated_by=user)
        if not coupon.duration:
            discount = amount * Coupon.objects.get(activated_by=user).discount / 100
            amount -= discount
        else:
            if coupon.activated_at + timezone.timedelta(days=coupon.duration) > timezone.now():
                discount = amount * Coupon.objects.get(activated_by=user).discount / 100
                amount -= discount
    return amount


def check_full_discount_for_premium(user):
    full_discount = False

    if Coupon.objects.filter(activated_by=user).exists():
        coupon = Coupon.objects.get(activated_by=user)

        if coupon.applies_to == 2:
            amount = settings.THREE_MONTH_AMOUNT
        elif coupon.applies_to == 3:
            amount = settings.ONE_YEAR_AMOUNT
        else:
            amount = 0

        if not coupon.duration:
            discount = amount * coupon.discount / 100
            amount -= discount
        else:
            if coupon.activated_at + timezone.timedelta(days=coupon.duration) > timezone.now():
                discount = amount * coupon.discount / 100
                amount -= discount

        if amount == 0:
            full_discount = True
    return full_discount

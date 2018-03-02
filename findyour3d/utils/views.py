import urllib
import calendar
import datetime
from django.utils import timezone

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

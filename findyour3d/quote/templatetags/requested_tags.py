from django import template
from django.utils import timezone

from findyour3d.quote.models import QuoteRequest

register = template.Library()


@register.simple_tag
def is_company_requested(company, user):
    now = timezone.now()

    if QuoteRequest.objects.filter(
        company=company, user=user, created_at__day=now.day, created_at__hour=now.hour).exists():
        return True
    else:
        return False


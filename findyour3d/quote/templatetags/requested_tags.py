from django import template

from findyour3d.quote.models import QuoteRequest

register = template.Library()


@register.simple_tag
def is_company_requested(company, user):
    if QuoteRequest.objects.filter(company=company, user=user).exists():
        return True
    else:
        return False


import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def send_templated_email(subject, email_template_name, email_context, recipients):

    html_content = render_to_string(email_template_name, email_context)
    text_content = strip_tags(html_content)

    massage = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [recipients])
    massage.attach_alternative(html_content, "text/html")

    try:
        massage.send()
    except Exception as e:
        logger.error(str(e))


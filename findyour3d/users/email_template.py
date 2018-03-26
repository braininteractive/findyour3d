import logging

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def send_templated_email(subject, email_template_name, email_context, recipients,
                         sender=None, bcc=None, fail_silently=False, files=None):

    if not sender:
        sender = settings.DEFAULT_FROM_EMAIL

    html_content = render_to_string(email_template_name, email_context)
    text_content = strip_tags(html_content)

    if isinstance(recipients, str):
        if recipients.find(','):
            recipients = recipients.split(',')
    elif not isinstance(recipients, list):
        recipients = [recipients]
    msg = EmailMultiAlternatives(subject, text_content, sender, recipients, bcc=bcc)
    msg.attach_alternative(html_content, "text/html")
    if files:
        if not isinstance(files, list):
            files = [files]
        for file in files:
            msg.attach_file(file)
    return msg.send(fail_silently)



from django.db import models

from findyour3d.users.email_template import send_templated_email

SUBJECT_CHOICES = (
    (0, 'Comment'),
    (1, 'Suggestion'),
    (2, 'Question'),
    (3, 'General Inquiry'),
    (4, 'Business Inquiry')
)


class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True, null=True)
    subject = models.IntegerField(choices=SUBJECT_CHOICES, default=0)
    body = models.TextField()
    is_sent = models.BooleanField(default=False)
    from_email = models.EmailField(default='no-reply@findyour3d.com')
    reply_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Message from {}".format(self.name)

    def save(self, *args, **kwargs):
        if not self.is_sent:
            if self.reply_text:
                send_templated_email('Your Request on Your3d',
                                     'email/contact_form_reply.html',
                                     {'reply_text': self.reply_text, 'name': self.name},
                                     [self.email, ])

                self.is_sent = True
        super().save(*args, **kwargs)

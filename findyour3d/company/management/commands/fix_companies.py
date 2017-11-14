import logging

from django.core.management.base import BaseCommand
from django.utils import timezone

from findyour3d.users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Adding valid payment for dummy companies'

    def handle(self, *args, **options):
        default_card = 'card_1ArI7LElSiayVU2xj6k589HC'
        stripe_id = 'cus_BDjavlKLrRcpf5'

        inactive_users = User.objects.filter(is_active=True, payment_active=False, user_type=2)
        print('To update: {}'.format(inactive_users.count()))
        for user in inactive_users:
            user.default_card = default_card
            user.stripe_id = stripe_id
            user.plan = 1
            user.paid_at = timezone.now()
            user.card_last = '4242'
            user.card_expiry = '1/2020'
            user.payment_active=True
            user.save()
        print('done!')

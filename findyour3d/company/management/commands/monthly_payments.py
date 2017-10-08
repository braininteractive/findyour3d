import logging

from django.core.management.base import BaseCommand
from findyour3d.payment.tasks import monthly_payments

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Charging Premium users'

    def handle(self, *args, **options):
        monthly_payments()

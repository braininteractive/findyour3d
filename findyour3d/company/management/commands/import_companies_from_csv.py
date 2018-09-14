from django.core.management.base import BaseCommand

import csv

from findyour3d.company.models import Company
from findyour3d.users.models import User


class Command(BaseCommand):
    help = 'Parsing giving CSV file and adding Users/Companies'

    def handle(self, *args, **options):
        csv_file = open('companies.csv', 'rb')   # fixme

        reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        to_create = []
        for row in reader:
            pass

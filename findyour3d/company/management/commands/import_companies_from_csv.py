from django.core.management.base import BaseCommand

import csv

from django.utils import timezone

from findyour3d.company.models import Company
from findyour3d.users.models import User


class Command(BaseCommand):
    help = 'Parsing giving CSV file and adding Users/Companies'

    def handle(self, *args, **options):
        user_type = 2
        count_ = 0
        with open('companies.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')

            for row in reader:
                username = password = row[0]
                company_name = row[1]
                display_name = row[2]
                address_line_1 = row[3]
                email = row[4]
                phone = row[5]
                website = row[6]
                description = row[7]
                material = row[10].split(',')
                top_printing_processes = row[11].split(',')

                if not User.objects.filter(username=username).exists():
                    user = User.objects.create(username=username,
                                               name=username,
                                               user_type=user_type,
                                               email=email,
                                               is_active=True,
                                               payment_active=True,
                                               plan=1,
                                               paid_at=timezone.now())
                    user.set_password(password)
                    user.save()

                    Company.objects.create(
                        name=company_name,
                        display_name=display_name,
                        address_line_1=address_line_1,
                        email=email,
                        phone=phone,
                        description=description,
                        website=website,
                        material=material,
                        top_printing_processes=top_printing_processes,
                        user=user)
                    count_ += 1
        print('Added: {}'.format(count_))

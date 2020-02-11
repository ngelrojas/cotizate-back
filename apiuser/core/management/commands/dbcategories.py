from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import CategoryCampaing


class Command(BaseCommand):
    help = 'create currencies'

    def success(self, message):
        return self.stdout.write(
                self.style.SUCCESS(message)
        )

    def warning(self, warning):
        return self.stdout.write(
                self.style.WARNING(warning)
        )

    def error(self, error):
        return self.stdout.write(
                self.style.ERROR(error)
        )

    def handle(self, *args, **options):
        self.warning(
                'if something goes wrong after fixtures installations,\
                        please use: python manage.py flush.'
        )

        with transaction.atomic():
            """create currencies"""
<<<<<<< HEAD
            currency_one = CategoryCampaing.objects.create(
                    name='Art'
            )
            currency_two = CategoryCampaing.objects.create(
                    name='Technology'
            )
=======
            CategoryCampaing.objects.create(name="Technology")
            CategoryCampaing.objects.create(name="Arts")
            CategoryCampaing.objects.create(name="Music")
>>>>>>> 0bee55a94b55adafd6453d10a40faee548f2b851
            self.success('categories created.')

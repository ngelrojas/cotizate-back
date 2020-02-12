from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Currency


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
            Currency.objects.create(
                    name='Bolivianos',
                    symbol='$Bs'
            )
            Currency.objects.create(
                    name='Dollares EE UU',
                    symbol='$Sus'
            )
            self.success('currencies created.')

from django.core.management.base import BaseCommand
from product.external_api import import_products


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        import_products()

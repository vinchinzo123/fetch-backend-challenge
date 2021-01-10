from django.core.management.base import BaseCommand
from payer.models import Payer

"""
add [DANNON, 300 points, 10/31 10AM] to user
add [UNILEVER, 200 points, 10/31 11AM] to user
add [DANNON, -200 points, 10/31 3PM] to user
add [MILLER COORS, 10,000 points , 11/1 2PM] to user
add [DANNON, 1000 points 11/2 2PM] to user
"""


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Payer.objects.all().delete()
        Payer.objects.create(client_name="DANNON")
        Payer.objects.create(client_name="UNILEVER")
        Payer.objects.create(client_name="MILLER COORS")

from django.core.management.base import BaseCommand
from transactions.models import Transaction
from payer.models import Payer
from datetime import datetime

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
        Transaction.objects.all().delete()
        DANNON = Payer.objects.create(client_name="DANNON")
        UNILEVER = Payer.objects.create(client_name="UNILEVER")
        MILLER_COORS = Payer.objects.create(client_name="MILLER COORS")
        Transaction.objects.create(
            company=DANNON,
            points=300,
            remaining_points=300,
            date=datetime(2020, 10, 31, 10),
        )
        DANNON.balance = DANNON.balance + 300
        DANNON.save()
        Transaction.objects.create(
            company=UNILEVER,
            points=200,
            remaining_points=200,
            date=datetime(2020, 10, 31, 11),
        )
        UNILEVER.balance = UNILEVER.balance + 200
        UNILEVER.save()
        Transaction.objects.create(
            company=DANNON,
            points=-200,
            remaining_points=-200,
            date=datetime(2020, 10, 31, 15),
        )
        DANNON.balance = DANNON.balance + -200
        DANNON.save()
        Transaction.objects.create(
            company=MILLER_COORS,
            points=10000,
            remaining_points=10000,
            date=datetime(2020, 11, 1, 14),
        )
        MILLER_COORS.balance = MILLER_COORS.balance + 10000
        MILLER_COORS.save()
        Transaction.objects.create(
            company=DANNON,
            points=1000,
            remaining_points=1000,
            date=datetime(2020, 11, 2, 14),
        )
        DANNON.balance = DANNON.balance + 1000
        DANNON.save()
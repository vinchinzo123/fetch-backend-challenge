from django.db import models
from payer.models import Payer
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    company = models.ForeignKey(Payer, on_delete=models.CASCADE)
    points = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    remaining_points = models.IntegerField(default=0)

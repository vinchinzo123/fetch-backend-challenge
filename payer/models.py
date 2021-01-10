from django.db import models

#  each transaction record contains: payer name(string), points (integer), transactionDate (Date).
# Create your models here.
class Payer(models.Model):
    client_name = models.CharField(max_length=140)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.client_name

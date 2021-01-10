from django.db import models

from payer.models import Payer
from transactions.models import Transaction

from rest_framework import serializers


class PayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payer
        fields = ["id", "client_name", "balance"]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "company", "points", "date", "paid", "remaining_points"]

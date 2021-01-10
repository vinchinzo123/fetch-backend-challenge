from api.serializers import PayerSerializer, TransactionSerializer
from payer.models import Payer
from transactions.models import Transaction
from django.http import Http404
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views
from rest_framework import viewsets

# Create your views here.
@api_view(["POST"])
def addPayerPoints(request):
    """
    Logic behind add-points/ route
    Example JSON request {"payer": "DANNON", "points": 1000, "date" : "11/2 2PM"}

    date value must be sent as a string following the convention given in the challenge example
      - "{month}/{day} {hour}{AM or PM}"
    """
    client = request.data["payer"]
    points = request.data["points"]
    date, time = request.data["date"].split(" ")
    month, day = date.split("/")
    midday = time[-2:]
    hour = time[:-2]
    payer = Payer.objects.get_or_create(client_name=client)[0]
    payer.balance = payer.balance + points
    payer.save()
    transaction_date = datetime.datetime.strptime(
        f"2020-{month}-{day} {hour}:00 {midday}", "%Y-%m-%d %I:%M %p"
    )
    transaction = (
        Transaction.objects.create(
            company=payer, points=points, date=transaction_date, remaining_points=points
        ),
    )

    return Response({"message": f"{points} points added to {client}"})


@api_view(["PUT"])
def removePayerPoints(request):
    points_to_remove = request.data["points"]
    transactions = Transaction.objects.filter(paid=False).order_by("date")
    company_paid_dict = {}
    for t in transactions:
        payer = t.company
        transaction_points = t.points
        company_paid_dict.setdefault(payer.client_name, 0)
        if points_to_remove >= transaction_points:
            t.paid = True
            t.remaining_points = 0
            t.save()
            points_to_remove = points_to_remove - transaction_points
            payer.balance = payer.balance - transaction_points
            payer.save()
            company_paid_dict[payer.client_name] = (
                company_paid_dict[payer.client_name] - transaction_points
            )
        else:
            t.remaining_points = t.remaining_points - points_to_remove
            t.save()
            payer.balance = payer.balance - points_to_remove
            payer.save()
            company_paid_dict[payer.client_name] = (
                company_paid_dict[payer.client_name] - points_to_remove
            )
            break
    payers = Payer.objects.all()
    deduct_calls = {}
    for i, (k, v) in enumerate(company_paid_dict.items()):
        deduct_calls[i] = {
            "payer": k,
            "points": v,
            "date": datetime.datetime.now().strftime("%m/%d %I:%M %p"),
        }
    return Response({"response": deduct_calls})


@api_view(["GET"])
def getPayerBalences(request):
    payers = Payer.objects.all()
    balances = {}
    for i, p in enumerate(payers):
        balances[i] = {"payer": p.client_name, "points": p.balance}
    return Response({"balances": balances})


class PayerViewset(viewsets.ModelViewSet):
    queryset = Payer.objects.all()
    serializer_class = PayerSerializer


class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

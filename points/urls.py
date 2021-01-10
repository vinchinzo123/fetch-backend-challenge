"""points URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import (
    TransactionViewset,
    PayerViewset,
    addPayerPoints,
    removePayerPoints,
    getPayerBalences,
)

router = routers.DefaultRouter()
router.register(r"transaction", TransactionViewset)
router.register(r"payer", PayerViewset)

urlpatterns = [
    path("add-points/", addPayerPoints),
    path("remove-points/", removePayerPoints),
    path("balances/", getPayerBalences),
    path("transactions/", TransactionViewset),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]

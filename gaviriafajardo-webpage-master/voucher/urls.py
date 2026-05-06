from django.urls import path

from voucher.views import validate_payment_view

app_name = "voucher"

urlpatterns = [
    path("validar/", validate_payment_view, name="validate-payment"),
]

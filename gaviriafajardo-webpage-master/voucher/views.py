from decimal import Decimal

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from voucher.constants import EPAYCO_EXPECTED_FIELDS, EPAYCO_SUCCESSFUL_TRANSACTION_STATUS
from voucher.models import Voucher
from voucher.utils import epayco_data_get_value


@csrf_exempt
def validate_payment_view(request):
    message, status_code = "OK", 200
    if request.method == "POST":
        data = dict(request.POST)
        if list(data.keys()).sort() == list(EPAYCO_EXPECTED_FIELDS).sort():
            transaction_code = epayco_data_get_value(data, "x_cod_transaction_state")
            Voucher.objects.create(
                successful_payment=(transaction_code == EPAYCO_SUCCESSFUL_TRANSACTION_STATUS),
                first_name=epayco_data_get_value(data, "x_customer_name", "No registra"),
                last_name=epayco_data_get_value(data, "x_customer_lastname", "No registra"),
                email=epayco_data_get_value(data, "x_customer_email", "No registra"),
                phone_number=epayco_data_get_value(data, "x_customer_movil", "No registra"),
                document_number=epayco_data_get_value(data, "x_customer_document", "No registra"),
                transaction_value=Decimal(epayco_data_get_value(data, "x_amount_ok", 0)),
                epayco_transaction_detail="{}-{}".format(
                    epayco_data_get_value(data, "x_transaction_state"),
                    epayco_data_get_value(data, "x_response_reason_text"),
                ),
                epayco_response=data,
            )
        else:
            message, status_code = "Ops! esto no lo esperaba.", 400
    else:
        message, status_code = "Ops! no puedes hacer esto.", 405
    return HttpResponse(message, status=status_code)

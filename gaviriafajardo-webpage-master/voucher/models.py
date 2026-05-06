from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.snippets.models import register_snippet

from commons.models import Audit


@register_snippet
class Voucher(Audit, models.Model):
    successful_payment = models.BooleanField(verbose_name="El pago se realizó correctamente", default=False)
    first_name = models.CharField(verbose_name="nombre", max_length=150, null=True, blank=True)
    last_name = models.CharField(verbose_name="apellido", max_length=150, null=True, blank=True)
    email = models.EmailField(verbose_name="correo electronico", max_length=254, null=True, blank=True)
    phone_number = models.CharField(verbose_name="numero telefónico", max_length=254, null=True, blank=True)
    document_number = models.CharField(verbose_name="número de documento", max_length=20, null=True, blank=True)
    transaction_value = models.DecimalField(
        verbose_name="valor de la transacción", max_digits=10, decimal_places=2, default=0
    )
    epayco_transaction_detail = models.CharField(
        verbose_name="descripción de la transacción de epayco", max_length=150, null=True, blank=True
    )
    epayco_response = models.JSONField(verbose_name="respuesta detallada de epayco", null=True)

    class Meta:
        verbose_name = "Voucher"
        verbose_name_plural = "Vouchers"

    def __str__(self):
        return self.first_name

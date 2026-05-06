from django.db import models
from wagtail.contrib.settings.registry import register_setting
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import RichTextField
from commons.models import Audit


@register_snippet
class Contact(Audit, models.Model):
    name = models.CharField(
        verbose_name="Nombres y apellidos",
        max_length=100
    )
    email = models.EmailField(
        verbose_name="Correo(s) de contacto",
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        verbose_name="Número(s) de contacto",
        max_length=20,
        blank=True
    )

    subject = models.CharField(
        verbose_name="Asunto",
        max_length=200,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Formulario de contacto"
        verbose_name_plural = "Formularios de contactos"

    def __str__(self):
        return self.name


@register_snippet
class Job(Audit, models.Model):

    name_applicant = models.CharField(
        verbose_name="Nombre del aplicante",
        max_length=100,
        blank=False
    )
    email_applicant = models.EmailField(
        verbose_name="Correo(s) de contacto del aplicante",
        null=True,
        blank=False,
    )
    phone_number_applicant = models.CharField(
        verbose_name="Número(s) de contacto del aplicante",
        max_length=20,
        blank=False,
    )

    subject_applicant = models.TextField(
        verbose_name="Asunto",
        max_length=200,
        null=True,
        blank=False,
    )
    file = models.FileField(
        verbose_name='Archivo',
        upload_to='Files/',
        max_length=255,
        null=True,
        blank=False,

    )

    class Meta:
        verbose_name = "Bolsa de empleo"
        verbose_name_plural = "Bolsa de empleos"

    def __str__(self):
        return self.name_applicant

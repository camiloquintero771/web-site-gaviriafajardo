from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.snippets.models import register_snippet

from commons.models import Audit


class DetailIndexPage(Page):
    content_title = models.CharField(
        verbose_name="titulo del contenido", max_length=150
    )
    content = RichTextField(verbose_name="contenido", null=True, blank=True)
    image = models.ImageField(
        verbose_name="imagen", upload_to="pages", null=True, blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("content_title"),
        FieldPanel("content"),
        FieldPanel("image"),
    ]

    @property
    def get_cover_images(self):
        return list(
            Carousel.active_objects.annotate(
                img=Concat(Value("/media/"), "image")
            ).values_list("img", flat=True)
        )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        image = ""
        if self.image:
            image = self.image.url
        context["title"] = self.content_title
        context["description"] = self.content
        context["image"] = image
        return context


@register_setting
class PageSettings(BaseSetting):
    logo_white = models.ImageField(
        verbose_name="logo para fondos oscuros", upload_to="logo_white"
    )
    logo_black = models.ImageField(
        verbose_name="logo para fondos oscuros", upload_to="logo_black"
    )
    contact_detail = RichTextField(
        verbose_name="Descripción sección contactanos", null=True, blank=True
    )
    footer_detail = RichTextField(
        verbose_name="Descripción sección pie de página", null=True, blank=True
    )
    address = RichTextField(
        verbose_name="Dirección(es) de ubicación", null=True, blank=True
    )
    phone_number = RichTextField(
        verbose_name="Número(s) de contacto", null=True, blank=True
    )
    email = RichTextField(verbose_name="Correo(s) de contacto", null=True, blank=True)
    top_trust_phrase = models.CharField(
        verbose_name="renglón superior de la frase de confianza",
        max_length=200,
        null=True,
        blank=True,
        editable=False,
    )
    bottom_trust_phrase = models.CharField(
        verbose_name="renglón inferior de la frase de confianza",
        max_length=200,
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        verbose_name = "Configuraciones de la página"
        verbose_name_plural = "Configuraciones de la página"


@register_snippet
class Service(Audit, Orderable, MPTTModel):
    name = models.CharField(verbose_name="nombre", max_length=150)
    image = models.ImageField(verbose_name="imagen", upload_to="services")
    description = RichTextField(verbose_name="descripción", null=True, blank=True)
    preview_in_home = models.BooleanField(
        verbose_name="visualizar en el carrousel de servicios del inicio", default=True
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="servicio padre",
    )
    slug = AutoSlugField(populate_from="name", editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name


@register_snippet
class Carousel(Audit, Orderable, models.Model):
    image = models.ImageField(verbose_name="Imagen", upload_to="carousel")

    class Meta:
        verbose_name = "Imagen del carousel principal"
        verbose_name_plural = "Imágenes del carousel principal"

    def __str__(self):
        return str(self.image.url)


@register_snippet
class New(Audit, Orderable, models.Model):
    title = models.CharField(verbose_name="Título", blank=False, max_length=150)
    subtitle = models.CharField(verbose_name="Subtítulo", max_length=150)
    content = RichTextField(verbose_name="Contenido", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen de la noticia", upload_to="carousel")
    slug = AutoSlugField(populate_from="title", editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.title


@register_snippet
class SocialNetwork(Audit, Orderable, models.Model):
    name = models.CharField(verbose_name="nombre", max_length=150, blank=False)
    icon_black = models.ImageField(
        verbose_name="Icono en negro", upload_to="socialnetwork", blank=True
    )
    icon_white = models.ImageField(
        verbose_name="Icono en blanco", upload_to="socialnetwork", blank=True
    )
    url = models.URLField(verbose_name="url de la red social", blank=False)

    class Meta:
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"

    def __str__(self):
        return self.name


@register_snippet
class Client(Audit, Orderable, models.Model):
    name = models.CharField(verbose_name="nombre", max_length=100, blank=False)
    image = models.ImageField(
        verbose_name="Imagen",
        upload_to="client",
        blank=True,
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class MenuItem(Audit, Orderable):
    title = models.CharField(verbose_name="título", max_length=150)
    url = models.URLField(verbose_name="redirección a url", null=True, blank=True)
    service = models.ForeignKey(
        "main.Service",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="redirección a servicio",
    )
    icon = models.ImageField(
        verbose_name="icono", upload_to="menu", null=True, blank=True
    )
    menu = ParentalKey(
        "main.Menu",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="menú asociado",
    )

    class Meta:
        verbose_name = "Item del menú"
        verbose_name_plural = "Items del menú"

    @property
    def get_redirect_url(self):
        if self.url:
            return str(self.url)
        elif self.service:
            return str(f"/servicio/{self.service.slug}/")
        return "/"

    def __str__(self):
        return self.title

    def clean(self):
        # Validate a single option
        available_options = ("url", "service")
        selected_options_counter = 0
        selected_options_label = []
        for option in available_options:
            field = self._meta.get_field(option)
            if field and getattr(self, option):
                selected_options_label.append(str(field.verbose_name))
                selected_options_counter += 1
        if selected_options_counter > 1:
            raise ValidationError(
                f"Seleccione solo una de las siguientes opciones ({', '.join(selected_options_label)})"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


@register_snippet
class Menu(Audit, Orderable, ClusterableModel):
    LOCATION_CHOICES = (("TOP", "Menú superior"), ("BOTTOM", "Menú inferior"))

    location = models.CharField(
        verbose_name="ubicación", max_length=50, choices=LOCATION_CHOICES, unique=True
    )
    description = models.TextField(verbose_name="descripción", null=True, blank=True)

    panels = (
        FieldPanel("location"),
        FieldPanel("description"),
        InlinePanel("menuitem_set", label="Items"),
    )

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menú"

    def __str__(self):
        return self.get_location_display()


@register_snippet
class Payment(Audit, Orderable, models.Model):
    name = models.CharField(verbose_name="nombre", max_length=100, blank=False)
    icon = models.ImageField(
        verbose_name="icono del medio de pago", upload_to="payment", blank=True
    )
    link = models.URLField(verbose_name="link del medio de pago", blank=False)

    class Meta:
        verbose_name = "Medio de pago"
        verbose_name_plural = "Medios de pagos"

    def __str__(self):
        return self.name

import random

from django.db import models
from django.db.models import Value, Func, F, Q
from django.db.models.functions import Concat
from django.shortcuts import redirect
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.core.models import Page

from commons.utils import get_serialized_query
from main.models import Service, New, Client, Carousel
from contact.forms import JobForm


class HomePage(RoutablePageMixin, Page):
    @property
    def get_cover_images(self):
        return list(
            Carousel.active_objects.annotate(img=Concat(Value("/media/"), "image")).values_list("img", flat=True)
        )

    @property
    def get_services(self):
        return get_serialized_query(
            Service.active_objects.filter(preview_in_home=True),
            {
                "title": "name",
                "img": Concat(Value("/media/"), "image", output_field=models.CharField()),
                "url": Concat(Value(str(self.url) + "servicio/"), F("slug"), output_field=models.CharField()),
            },
        )

    @property
    def get_news(self):
        return get_serialized_query(
            New.active_objects.order_by("-created_at")[:10],
            {
                "text_bold": "title",
                "text_small": Func(
                    F("created_at"), Value("DD/MM/YYYY"), function="to_char", output_field=models.CharField()
                ),
                "description": "subtitle",
                "img": Concat(Value("/media/"), "image", output_field=models.CharField()),
                "url": Concat(Value(str(self.url) + "noticia/"), F("slug"), output_field=models.CharField()),
            },
        )

    @property
    def get_clients(self):
        return Client.active_objects.all()

    @property
    def get_contact_center(self):
        return Service.active_objects.filter(name__iexact="contact center").first()

    @route(r"^servicio/(?P<service>[\w-]+)/$")
    def service_detail(self, request, service=None):
        try:
            service = Service.active_objects.get(slug=service)
        except Service.DoesNotExist:
            return redirect(self.url)
        return self.render(
            request,
            context_overrides={
                "page": self,
                "title": service.name,
                "description": service.description,
                "image": service.image.url,
                "cards": get_serialized_query(
                    Service.active_objects.filter(parent_id=service.id),
                    {
                        "title": "name",
                        "img": Concat(Value("/media/"), "image", output_field=models.CharField()),
                        "url": Concat(Value(str(self.url) + "servicio/"), F("slug"), output_field=models.CharField()),
                    },
                ),
            },
            template="main/detail_index_page.html",
        )

    @route(r"^noticia/(?P<new>[\w-]+)/$")
    def new_detail(self, request, new=None):
        try:
            new = New.active_objects.get(slug=new)
        except New.DoesNotExist:
            return redirect(self.url)
        return self.render(
            request,
            context_overrides={
                "page": self,
                "title": new.title,
                "description": new.content,
                "image": new.image.url,
            },
            template="main/detail_index_page.html",
        )

    @route(r"^buscar-coincidencias/$")
    def find_matches(self, request):
        all_matches = []
        search_by = request.GET.get("search", "")
        if search_by:
            news = get_serialized_query(
                New.objects.filter(
                    Q(title__icontains=search_by) | Q(subtitle__icontains=search_by) | Q(content__icontains=search_by)
                ),
                {
                    "title": "title",
                    "type": Value("Noticia", output_field=models.CharField()),
                    "img": Concat(Value("/media/"), "image", output_field=models.CharField()),
                    "url": Concat(Value(str(self.url) + "noticia/"), F("slug"), output_field=models.CharField()),
                },
            )
            services = get_serialized_query(
                Service.objects.filter(Q(name__icontains=search_by) | Q(description__icontains=search_by)),
                {
                    "title": "name",
                    "type": Value("Servicio", output_field=models.CharField()),
                    "img": Concat(Value("/media/"), "image", output_field=models.CharField()),
                    "url": Concat(Value(str(self.url) + "servicio/"), F("slug"), output_field=models.CharField()),
                },
            )
            all_matches = news + services
        all_matches = random.sample(all_matches, k=len(all_matches))
        return self.render(
            request,
            context_overrides={
                "page": self,
                "search_by": search_by,
                "all_matches": all_matches,
            },
            template="home/search_results_page.html",
        )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['job'] = JobForm
        return context

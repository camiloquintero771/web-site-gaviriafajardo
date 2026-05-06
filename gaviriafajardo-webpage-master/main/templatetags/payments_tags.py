from django import template

from main.models import SocialNetwork, Payment

register = template.Library()


@register.simple_tag(takes_context=True)
def get_payment_methods(context):
    context["payment_methods"] = Payment.active_objects.all()
    return ""

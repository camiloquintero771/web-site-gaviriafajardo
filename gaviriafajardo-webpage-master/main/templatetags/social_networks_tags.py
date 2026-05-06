from django import template

from main.models import SocialNetwork

register = template.Library()


@register.simple_tag(takes_context=True)
def get_social_networks(context):
    context["social_networks"] = SocialNetwork.active_objects.all()
    return ""

from django import template

from main.models import SocialNetwork, Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def get_menus(context):
    menus_query = Menu.active_objects.all()
    menus_dict = {}
    for menu in menus_query:
        menus_dict.update({menu.location: menu.menuitem_set.filter(is_active=True).order_by("sort_order")})
    context["menus"] = menus_dict
    return ""

from django import template
from django.conf import settings
from django.utils.text import capfirst
register = template.Library()

@register.filter
def menu_class(item, url):
    return 'active' if item.url == url else ''

@register.filter
def menu1_class(item, url):
    return " ".join(['active' if item.url == url else '', 'sub-menu sub-menu-1' if item.submenu else ''])

@register.filter
def menu2_class(item, url):
    return " ".join(['active' if item.url == url else '', 'sub-menu sub-menu-2' if item.submenu else ''])


@register.simple_tag
def flag(lang):
    name = capfirst(lang['name_local'])
    return '<img src="%simg/flags/%s.png" class="flag" alt="%s" /><span class="flag"> %s</span>' % \
           (settings.STATIC_URL, lang['code'], name, name)
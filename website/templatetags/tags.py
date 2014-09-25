from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def active(request, pattern):
    if pattern in request.path:
        return 'active'
    return ''

# settings value
# usage: {% settings_value "LANGUAGE_CODE" %}
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

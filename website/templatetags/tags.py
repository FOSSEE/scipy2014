from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    if pattern in request.path:
        return 'active'
    return ''

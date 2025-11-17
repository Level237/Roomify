from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active_link(context, pattern):
    request = context['request']
    if pattern in request.path:
        return 'active'
    return ''
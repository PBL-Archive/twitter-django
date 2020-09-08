from django import template
import re

register = template.Library()


@register.filter
def removeTags(value):
    value = re.sub(r'@\S*', '', value)
    # value = re.sub(r'\s*', ' ', value)
    return value

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='find_and_replace')
@stringfilter
def find_and_replace(value, arg):
    if value.replace('$', arg) is not None:
        return value.replace('$', arg)
    else:
        return "0"


@register.filter(name='divide_by')
@stringfilter
def divide_by(value, arg):
    try:
        return int(value)//int(arg)
    except:
        return 0
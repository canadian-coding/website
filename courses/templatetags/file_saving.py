from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def filefilter(value):
    return value.replace("`", "") # removes backticks from files to keep them from escaping the js
from django import template

register = template.Library()

@register.filter
def multiple(value, arg):
    """ Multiplies value by the argument (e.g., price * quantity) """
    try:
        return value * arg
    except (TypeError, ValueError):
        return value
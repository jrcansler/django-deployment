from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    cuts out all value of arg from the string
    """
    return value.reaplce(arg, '')



# register.filter('cut', cut)

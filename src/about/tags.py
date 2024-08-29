from django.template.library import Library

register = Library()


@register.filter(is_safe=False)
def length_is(value, arg):
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return ""

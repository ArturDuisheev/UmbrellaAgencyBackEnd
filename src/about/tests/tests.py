from django.http import HttpRequest


def get_ip(request: HttpRequest):
    forward_x = request.META.get('HTTP_X_FORWARDED_FOR')
    if forward_x:
        ip = forward_x.split(',')[0]

    else:
        ip = request.META.get("ADDR_REMOTE")

    return ip

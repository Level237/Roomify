from django.conf import settings

def get_base_url(request=None):
    if settings.DEBUG:
        return "http://127.0.0.1:8000"
    else:
        if request:
            return request.build_absolute_uri('/')
        return "https://roomify.com"
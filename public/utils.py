from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2

def get_country_from_ip(request):
    ip,is_routable=get_client_ip(request)
    
    if ip is None:
        return None
    g= GeoIP2()
    
    try:
        country=g.country_name(ip)
        return country
    except Exception:
        return None
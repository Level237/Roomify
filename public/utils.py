from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2

def get_country_from_ip(request):
    
    ip,is_routable=get_client_ip(request)
    print(ip)
    if ip in ('127.0.0.1', '::1', None):
        ip = '8.8.8.8'  # IP Google, pour tester (retournera USA)

    g = GeoIP2()
    print(g.country_name(ip))
    try:
        country=g.country_name(ip)
        
        return country
    except Exception:
        return None
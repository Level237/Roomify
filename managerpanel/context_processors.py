

from hotels.models import Hotel


def get_recents_hotel_context(request):
    get_hotels_recents=Hotel.objects.all().filter(manager=request.user).order_by('-created_at')[:3]
    return {'hotels_recents':get_hotels_recents}
    
    
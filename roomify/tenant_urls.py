
from django.urls import path, include



urlpatterns = [
    path('', include('hotels.urls', namespace='hotels')),
]
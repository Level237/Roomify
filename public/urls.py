from django.urls import path
from . import views

app_name="public"

urlpatterns = [
    path('', views.public_home_view, name='home'),

    path('signup/', views.signup, name='signup'),
]
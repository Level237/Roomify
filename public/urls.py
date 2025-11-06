from django.urls import path
from . import views


urlpatterns = [
    path('', views.public_home_view, name='home'),

    #path('signup/', views.TenantSignupView.as_view(), name='signup'),
]
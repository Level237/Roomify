from django.urls import path
from . import views

app_name= 'customerpanel'
urlpatterns = [
    path('dashboard/',views.dashboard_customer,name="customer_dashboard")
]

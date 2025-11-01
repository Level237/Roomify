from django.urls import path
from . import views

app_name="managerpanel"
urlpatterns = [
    path("dashboard/",views.dashboard_manager,name="manager_dashboard")
]

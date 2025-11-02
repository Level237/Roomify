from django.urls import path
from . import views

app_name="managerpanel"
urlpatterns = [
    path("dashboard/",views.dashboard_manager,name="manager_dashboard"),
    path("create-hotel/<int:hotel_id>",views.create_hotel,name="create_hotel"),
]

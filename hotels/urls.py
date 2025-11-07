from django.urls import path
from . import views

app_name="hotels"
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard")
]

from django.urls import path
from . import views

app_name="hotels"
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("login/",views.tenant_login,name="login"),
    path("manage/rooms/",views.room_list,name="manage-rooms"),
    path("forgot-password/",views.forgot_password,name="forgot-password"),
]

from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path('register/',views.register_user,name="register"),
    path('login/',views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("set-password/<int:user_id>/",views.SetPasswordForm,name="hotelier_set_password")
]
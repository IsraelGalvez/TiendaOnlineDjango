import imp
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('login/',views.Login.as_view(),name="user-login"),
    path('logout/',views.LogoutView.as_view(),name="user-logout"),
    path('register/',views.UserRegisterView.as_view(),name="user-register"),
    path('cambiarContrasena/',views.CambiarContrasenaView.as_view(),name="user-new-password"),
]
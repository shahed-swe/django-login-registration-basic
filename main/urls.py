from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.myregister, name="myregister"),
    path('login/', views.mylogin, name="mylogin"),
    path('logout/', views.mylogout, name="mylogout"),
]

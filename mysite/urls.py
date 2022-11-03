from django.urls import path
from . import views


urlpatterns = [
    path("",views.indexall,name="index"),
    path("dashboard",views.dashboard,name="dashboard"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('collectors/',views.collectors,name="collectors"),
    path('register-donors/',views.registerdonors,name="Register Donors"),
    path('register-collectors/',views.registercollectors,name="Register Collectors"),
    path('hospital-request/', views.hospitalrequest, name = "Hospital Requests"),
    path('register-patients/',views.registerpatients,name="Register Patients"),
]
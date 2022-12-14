from django.urls import path
from . import views


urlpatterns = [
    path("",views.indexall,name="index"),
    path("dashboard",views.dashboard,name="dashboard"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('collectors/',views.collectors,name="collectors"),
    path('register-collectors/',views.registercollectors,name="Register Collectors"),
    path('donors/',views.donors, name= "Donors"),
    path('donors/register-donors/',views.registerdonors,name="registerdonors"),
    path('patients/',views.patients,name="patients"),
    path('patients/register-patients/',views.patients,name="patients"),
    path('rbc-stock/',views.rbcstock,name="rbcstock"),
    path('hospital-request/', views.hospitalrequest, name = "Hospital Requests"),
    path('register-patients/',views.registerpatients,name="Register Patients"),
]
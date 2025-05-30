from django.urls import path
from . import views

urlpatterns = [
    path('tenants/dashboard', views.tenants_dashboard, name='tenants_dashboard'),
    path('tenants/registration', views.tenants_registration, name='tenants_registration')
]
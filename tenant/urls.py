from django.urls import path
from . import views

urlpatterns = [
    path('tenants/registration', views.tenants_registration, name='tenants_registration')
]
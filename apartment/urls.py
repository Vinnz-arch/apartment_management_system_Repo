from django.urls import path
from . import views

app_name = 'apartment_unit'

urlpatterns = [
      path('tenants/unitInfo', views.unit_info, name='unit_info'),
      path('apartment/units/<int:unit_id>/', views.get_unit_details, name='get_unit_details'),
] 
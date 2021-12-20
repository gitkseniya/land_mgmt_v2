from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('units', views.units, name='units'),
    path('owner/<int:owner_id>/', views.owner, name='owner'),
    path('unit/<int:unit_id>/', views.unit, name='unit'),

]

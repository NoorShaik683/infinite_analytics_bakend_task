from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('picnic_spots/<int:location_id>/', views.picnic_spots, name='picnic_spots'),
    path('subscribe/<int:location_id>/', views.subscribe, name='subscribe'),
]

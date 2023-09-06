from .import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('event/<str:event_id>/', views.event, name='event'),
    path('map/', views.map, name='map'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/upcoming/', views.upcoming_events_view, name='upcoming_events'),
    path('events/past/', views.past_events_view, name='past_events'),
    path('event/<int:event_id>/', views.event_details_view, name='event_details'),
    path('contact/', views.contact_view, name='contact'),
]

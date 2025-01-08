from django.urls import path
from .views import produce_event_api

urlpatterns = [
    path('produce/', produce_event_api, name='produce_event'),
]

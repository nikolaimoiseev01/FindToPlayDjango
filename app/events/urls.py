from django.urls import path

from events.views import EventsAPIView

urlpatterns = [
    path('', EventsAPIView.as_view(), name='events')
]

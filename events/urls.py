from django.urls import path

from events import views
from events.views import EventsAPIView

urlpatterns = [
    path('', EventsAPIView.as_view(), name='events')
]

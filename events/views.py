from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event, Sport
from events.serializers import EventSerializer, SportSerializer


class EventsAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response({'events': serializer.data})

    def post(self, request):
        event_new = Event.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            date=request.data['date'],
            location=request.data['location'],
            user=request.user,
            sport=request.data['sport']
        )
        return Response({'event': EventSerializer(event_new).data})


class SportAPIView(APIView):
    def get(self, request):
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data)


# Create your views here.
def index(request):
    return HttpResponse('Hello world!')

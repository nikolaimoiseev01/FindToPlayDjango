from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    date = serializers.DateTimeField()
    location = serializers.CharField(max_length=200)


class SportSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

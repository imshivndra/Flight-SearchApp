from rest_framework import serializers
from .models import FlightDetails

class FlightDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlightDetails
        fields=("id","number","departure_city", "departure_time","arrival_city","arrival_time")
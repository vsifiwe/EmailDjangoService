from .models import Human, Track
from rest_framework import serializers


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
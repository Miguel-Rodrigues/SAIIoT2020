# AccelKartServer/serializers.py
from rest_framework import serializers
from .models import Student


class RemoteIMUSensorISerializer(serializers.ModelSerializer):
    class Meta:
        model = "Remote IMU Sensor"
        fields = ("GyroX", "GyroY", "GyroZ", "AcellerometerX", "AcellerometerY", "AcellerometerZ", "CompassX", "CompassY", "CompassZ", "Button1", "Button2")
from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class MeasurementNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class SensorDetailedSerializer(serializers.ModelSerializer):
    measurements = MeasurementNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurements']

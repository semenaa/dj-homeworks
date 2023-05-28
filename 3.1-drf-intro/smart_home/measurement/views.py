# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorListCreateAPI(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateAPI(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

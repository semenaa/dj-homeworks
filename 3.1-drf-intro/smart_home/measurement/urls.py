from django.urls import path

from measurement.views import SensorListCreateAPI, SensorRetrieveUpdateAPI, MeasurementCreateAPI

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreateAPI.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateAPI.as_view()),
    path('measurements/', MeasurementCreateAPI.as_view()),
]

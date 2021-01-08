# AccelKartServer/views.py
from rest_framework import generics
from .models import RemoteIMUSensor
from .serializers import RemoteIMUSensorISerializer


class KartAPI(generics.ListCreateAPIView):
    queryset = RemoteIMUSensor.objects.all()
    serializer_class = RemoteIMUSensorISerializer

class KartAPIDetail(generics.CreateAPIView):
    queryset = RemoteIMUSensor.objects.all()
    serializer_class = RemoteIMUSensorISerializer

# Request -> RPI
# {
#     "XAccel" : -100,
#     "YAccel" : -100,
#     "ZAccel" : -100,
#     "compassX" : -100,
#     "compassY" : -100,
#     "compassZ" : -100,
#     "Button1" : true,
#     "Button2" : false   
# }

# Response -> ESP32
# {
#     "Status" : "OK|ERROR",
#     ""
# }
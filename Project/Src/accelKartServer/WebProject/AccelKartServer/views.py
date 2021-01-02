# AccelKartServer/views.py
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


class KartAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

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
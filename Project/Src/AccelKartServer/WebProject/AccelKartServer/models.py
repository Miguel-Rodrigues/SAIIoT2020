from rest_framework.fields import BooleanField, CharField, DecimalField
from rest_framework.serializers import Serializer

class SensorData:
    name: str = ""
    pitch: float = 0
    roll: float = 0
    heading: float = 0
    button1: bool = False
    button2: bool = False

    def __init__(self, dict = None):
        if (dict != None):
            self.name = dict["name"]
            self.pitch = float(dict["pitch"])
            self.roll = float(dict["roll"])
            self.heading = float(dict["heading"])
            self.button1 = dict["button1"].lower() == "true"
            self.button2 = dict["button2"].lower() == "true"
            pass
        pass
    pass

class SensorDataSerializer(Serializer):
    name = CharField(default="")
    pitch = DecimalField(50, 20,default = 0)
    roll = DecimalField(50, 20, default = 0)
    heading = DecimalField(50, 20, default = 0)
    button1 = BooleanField(default = False)
    button2 = BooleanField(default = False)

    class Meta:
         model = SensorData
         pass
    pass
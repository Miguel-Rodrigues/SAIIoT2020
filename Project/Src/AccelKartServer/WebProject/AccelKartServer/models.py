from rest_framework.fields import BooleanField, CharField, DecimalField
from rest_framework.serializers import Serializer

class Point3D:
    x: float = 0
    y: float = 0
    z: float = 0

    def __init__(self, dict = None):
        if (dict != None):
            self.x = dict["x"]
            self.y = dict["y"]
            self.z = dict["z"]
            pass
        pass

    pass

class SensorData:
    name: str = ""
    accel: Point3D()
    gyro: Point3D()
    compass: Point3D()
    pitch: float = 0
    roll: float = 0
    heading: float = 0
    button1: bool = False
    button2: bool = False

    def __init__(self, dict = None):
        if (dict != None):
            self.name = dict["name"]
            self.accel = Point3D(dict["accel"])
            self.gyro = Point3D(dict["gyro"])
            self.compass = Point3D(dict["compass"])
            self.pitch = dict["pitch"]
            self.roll = dict["roll"]
            self.heading = dict["heading"]
            self.button1 = dict["button1"]
            self.button2 = dict["button2"]
            pass
        pass

    pass

class Point3DSerializer(Serializer):
    x: DecimalField(10, 1, default = 0)
    y: DecimalField(10, 6, default = 0)
    z: DecimalField(10, 6, default = 0)

    class Meta:
        model = Point3D
        pass
    pass

class SensorDataSerializer(Serializer):
    name = CharField(default="")
    accel = Point3DSerializer()
    gyro = Point3DSerializer()
    compass = Point3DSerializer()
    pitch = DecimalField(10, 6, default = 0)
    roll = DecimalField(10, 6, default = 0)
    heading = DecimalField(10, 6, default = 0)
    button1 = BooleanField(default = False)
    button2 = BooleanField(default = False)

    class Meta:
         model = SensorData
         pass
    pass
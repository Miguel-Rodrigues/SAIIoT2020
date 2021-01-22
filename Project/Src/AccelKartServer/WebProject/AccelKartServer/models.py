from rest_framework import serializers

class Point3D:
    x: float = 0
    y: float = 0
    z: float = 0
    pass
class Point3DSerializer(serializers.Serializer):
    x: serializers.DecimalField(3, 5, default = 0)
    y: serializers.DecimalField(3, 5, default = 0)
    z: serializers.DecimalField(3, 5, default = 0)
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
    pass

class SensorDataSerializer(serializers.Serializer):
    name = serializers.CharField(default="")
    accel = Point3DSerializer(many=False, default=Point3D())
    gyro = Point3DSerializer(many=False, default=Point3D())
    compass = Point3DSerializer(many=False, default=Point3D())
    pitch = serializers.DecimalField(3, 5, default = 0)
    roll = serializers.DecimalField(3, 5, default = 0)
    heading = serializers.DecimalField(3, 5, default = 0)
    button1 = serializers.BooleanField(default = False)
    button2 = serializers.BooleanField(default = False)
    pass
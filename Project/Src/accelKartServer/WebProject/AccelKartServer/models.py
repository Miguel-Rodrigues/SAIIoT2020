# AccelKartServer/models.py
from django.db import models


class RemoteIMUSensor(models.Model):
    AccessToken = models.CharField(max_length=255)
    RemoteName = models.CharField(max_length=255)

    GyroX = models.DecimalField(max_digits=3, decimal_places= 5)
    GyroY = models.DecimalField(max_digits=3, decimal_places= 5)
    GyroZ = models.DecimalField(max_digits=3, decimal_places= 5)
    AcellerometerX = models.DecimalField(max_digits=3, decimal_places= 5)
    AcellerometerY = models.DecimalField(max_digits=3, decimal_places= 5)
    AcellerometerZ = models.DecimalField(max_digits=3, decimal_places= 5)
    CompassX = models.DecimalField(max_digits=3, decimal_places= 5)
    CompassY = models.DecimalField(max_digits=3, decimal_places= 5)
    CompassZ = models.DecimalField(max_digits=3, decimal_places= 5)
    Button1 = models.BooleanField()
    Button2 = models.BooleanField()
    
    def __str__(self):
        return self.RemoteName
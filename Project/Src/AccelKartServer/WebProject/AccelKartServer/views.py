# AccelKartServer/views.py
import sys
import asyncio
import logging
from . import models
from .services.KartDriverService import KartDriverService
from django.template.response import TemplateResponse
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

# https://stackoverflow.com/questions/37916077/django-run-code-on-application-start-but-not-on-migrations
kartDriverService: KartDriverService
if ('makemigrations' not in sys.argv and 'migrate' not in sys.argv):
    kartDriverService = KartDriverService()

logger = logging.getLogger(__name__)

@api_view(['GET'])
def joypad(request):
    logger.info("GET '/'")
    response = TemplateResponse(request, 'KartAPIControls.html', {})
    return response

@api_view(['GET'])
def apiOverview(request):
    logger.info("GET '/api/apioverview'")
    api_urls = {
        "VirtualKartJoypad" : "/",
        "APIOverview"       : "/api/",
        "MoveKart"          : "/api/moveKart/",
        "OpenAPI"           : "/api/openAPI/",
        "SwaggerUI"         : "/api/swagger/",
    }

    return Response(api_urls)

@api_view(['POST'])
def moveKart(request):
    logger.info("POST '/api/moveKart'")

    try:
        model = models.SensorDataSerializer(data = request.data)
        if (model.is_valid()):
            logger.debug("SensorData model is valid")
            data: models.SensorData = models.SensorData(request.data)
            kartDriverService.moveKart(data)
            return Response({"Status" : "OK"})
        else:
            raise serializers.ValidationError({"Status": "NOT OK", "Fields": model.errors})
    except:
            raise APIException({"Status": "NOT OK", "Exception" : sys.exc_info()})

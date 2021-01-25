# AccelKartServer/views.py
from django.conf import settings
from django.http.response import JsonResponse
from django.template.response import TemplateResponse
from rest_framework import serializers
from rest_framework.exceptions import bad_request
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.KartDriverService import KartDriverService
from . import models
import logging
import sys

# https://stackoverflow.com/questions/37916077/django-run-code-on-application-start-but-not-on-migrations
kartDriverService: KartDriverService
if (settings.RUNTIME):
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
    model = models.SensorDataSerializer(data = request.data)
    if (model.is_valid()):
        logger.debug("SensorData model is valid")
        data: models.SensorData = models.SensorData(request.data)
        kartDriverService.moveKart(data)
        return JsonResponse({"Status" : "OK"})
    else:
        raise serializers.ValidationError({"Status": "NOT OK", "Fields": model.errors})
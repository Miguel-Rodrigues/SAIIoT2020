# AccelKartServer/views.py
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.KartDriverService import KartDriverService
from django.template.response import TemplateResponse

import sys

kartDriverService: KartDriverService = KartDriverService()

@api_view(['GET'])
def joypad(request):
    response = TemplateResponse(request, 'KartAPIControls.html', {})
    return response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "VirtualKartJoypad" : "/",
        "APIOverview"       : "/api/",
        "MoveKart"          : "/api/moveKart/",
        "OpenAPI"           : "/api/openAPI/",
        "SwaggerUI"         : "/api/swagger/",
    }

    return Response(api_urls)

@api_view(['POST'])
def moveKart(self, request):
    self.kartDriverService.moveKart(request)
    return JsonResponse({"Status" : "OK"})
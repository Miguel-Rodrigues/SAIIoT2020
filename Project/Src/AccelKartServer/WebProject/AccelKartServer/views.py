# AccelKartServer/views.py
from django.http.response import JsonResponse
from django.views.generic.base import View
from rest_framework.generics import ListCreateAPIView
from .services.KartDriverService import KartDriverService
from django.template.response import TemplateResponse

import sys

class KartAPI(ListCreateAPIView):

    kartDriverService: KartDriverService

    def __init__(self):
        self.kartDriverService = KartDriverService()
        pass

    def get(self, request):
        response = TemplateResponse(request, 'KartAPIControls.html', {})
        return response

    def post(self, request):
        # try:
        self.kartDriverService.updateKartMovement(request)
        return JsonResponse({"Status" : "OK"})

        # except:
        #     return JsonResponse({
        #         "Status" : "NOK",
        #         "Reasons" : sys.exc_info()
        #     })
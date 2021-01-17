# AccelKartServer/views.py
from django.http.response import JsonResponse
from rest_framework import generics
from django.template.response import TemplateResponse

class KartAPI(generics.ListCreateAPIView):

    def get(self, request):
        response = TemplateResponse(request, 'KartAPIControls.html', {})
        return response

    def post(self, request):
        
        return JsonResponse({"Status" : "OK"})
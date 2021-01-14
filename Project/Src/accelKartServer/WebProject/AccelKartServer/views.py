# AccelKartServer/views.py
from rest_framework import generics
from django.template.response import TemplateResponse

class KartAPI(generics.ListCreateAPIView):

    def get(self, request):
        response = TemplateResponse(request, 'KartAPIControls.html', {})
        return response

    def post(self, request):
        return Response({Hello : "World"})
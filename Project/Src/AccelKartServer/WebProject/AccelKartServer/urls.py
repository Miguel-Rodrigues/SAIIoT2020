from django.urls import path
from django.views.generic.base import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('/', views.joypad, name="Kart Virtual Joypad"),
    path('/api/', views.apiOverview, name="API Overview"),
    path('/api/moveKart/', views.moveKart, name="Move Kart"),
    path('/api/openapi/', get_schema_view(title="Accelerometer Kart Service OpenAPI", description="API for developers to use our kart service"), name='openapi-schema'),
    path('/api/swagger/', TemplateView.as_view(template_name='documentation.html', extra_context={'schema_url':'openapi-schema'}), name='Swagger UI'),
] 
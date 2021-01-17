from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from AccelKartServer import views

urlpatterns = [
    path('', views.KartAPI.as_view())
]
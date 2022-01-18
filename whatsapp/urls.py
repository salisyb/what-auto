from django.urls import path
from .views import readWhatsapp


urlpatterns = [
    path("",  readWhatsapp)
]

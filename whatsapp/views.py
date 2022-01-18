from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET', 'POST'])
def readWhatsapp(request):
    if request.method == 'POST':
        print(request.data)
        return JsonResponse({"reply": "hello World"})
    return JsonResponse({"message": "Hello, world!"})

import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def hello(request):
    print(request)
    token = request.GET.get('token', None)
    if token == 'box1':
        return HttpResponse("47,50,60,100")
    else:
        return JsonResponse({"error": "Invalid token"})


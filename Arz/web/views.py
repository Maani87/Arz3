from django.shortcuts import render
from django.http import JsonResponse
import json

def submit_expense(request):
    """user submits an expense"""

    print ("im in submit expense")
    print (request.POST)

    return JsonResponse({
        "status": "ok", 
    },encoder=JASONEncoder)

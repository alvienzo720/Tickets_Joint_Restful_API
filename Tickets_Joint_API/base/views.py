from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.



def endpoints(request):
    data = ['/tickets', 'tickets/:ticketname']
    return JsonResponse(data, safe=False)

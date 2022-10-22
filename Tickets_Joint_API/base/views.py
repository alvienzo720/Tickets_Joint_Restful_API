from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.



def endpoints(request):
    data = ['/tickets', 'tickets/:ticketname']
    return JsonResponse(data, safe=False)


def ticket_list(request):
    data = ['Nyege-Nyege', 'Bayimba-Festival', 'Roast&Rhyme']
    return JsonResponse(data, safe=False)


def ticket_details(request, ticketname):
    data = ticketname
    return JsonResponse(data, safe=False)
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket
# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/tickets', 'tickets/:ticketname']
    return Response(data)

@api_view(['GET'])
def ticket_list(request):
    tickets = Ticket.objects.all()
    return Response(tickets)

@api_view(['GET'])
def ticket_details(request, ticketname):
    data = ticketname
    return Response(data)
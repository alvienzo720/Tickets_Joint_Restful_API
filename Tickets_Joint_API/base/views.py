from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicektSerializer
# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/tickets', 'tickets/:ticketname']
    return Response(data)

@api_view(['GET'])
def ticket_list(request):
    tickets = Ticket.objects.all()
    serializer = TicektSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ticket_details(request, ticketname):
    ticket = Ticket.objects.get(ticket_name=ticketname)
    seralizer = TicektSerializer(ticket, many=False)
    return Response(seralizer.data)
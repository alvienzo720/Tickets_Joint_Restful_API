from django.shortcuts import render, redirect
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

@api_view(['GET','POST'])
def ticket_list(request):
    # handles GET requests
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query == None:
            query = ''
        tickets = Ticket.objects.filter(ticket_name__icontains=query)
        serializer = TicektSerializer(tickets, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        ticket = Ticket.objects.create(
            ticket_name=request.data['ticket_name'],
            price=request.data['price'],
            date=request.data['date'],
            ticket_owner=request.data['ticket_owner']
            )
        serializer = TicektSerializer(ticket, many=False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def ticket_details(request, ticketname):
    ticket = Ticket.objects.get(ticket_name=ticketname)
    if request.method == 'GET':
        seralizer = TicektSerializer(ticket, many=False)
        return Response(seralizer.data)

    if request.method == 'PUT':
        ticket.ticket_name == request.data['ticket_name']
        ticket.price = request.data['price']
        ticket.data = request.data['date']
        ticket.ticket_owner = request.data['ticket_owner']
        ticket.save()

        seralizer = TicektSerializer(ticket, many=False)
        return Response((seralizer.data))

    if request.method == 'DELETE':
        ticket.delete()
        return Response('Ticket Deleted')




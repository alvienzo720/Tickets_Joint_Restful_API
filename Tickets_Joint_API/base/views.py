from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ticket, Client
from .serializers import TicektSerializer, ClientSerializer

# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/tickets', 'tickets/:ticketname', '/clients', 'clients/:fullname']
    return Response(data)


class TicketList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query == None:
            query = ''
        tickets = Ticket.objects.filter(ticket_name__icontains=query)
        serializer = TicektSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        ticket = Ticket.objects.create(
        ticket_name=request.data['ticket_name'],
        price=request.data['price'],
        date=request.data['date'],
        ticket_owner=request.data['ticket_owner']
           )
        serializer = TicektSerializer(ticket, many=False)
        return Response(serializer.data)


class TicketDetails(APIView):

    def get_object(self, ticketname):
        try:
            return Ticket.objects.get(ticket_name=ticketname)
        except Ticket.DoesNotExisit:
            raise JsonResponse('Ticket Dosent Exist ! ')

    def get(self, request, ticketname):
        ticket = self.get_object(ticketname)
        serializer = TicektSerializer(ticket, many=False)
        return Response(serializer.data)


    def put(self, request, ticketname):
        ticket = self.get_object(ticketname)
        ticket.ticket_name = request.data['ticket_name']
        ticket.price = request.data['price']
        ticket.data = request.data['date']
        ticket.ticket_owner = request.data['ticket_owner']
        ticket.save()

        serializer = TicektSerializer(ticket, many=False)
        return Response(serializer.data)


    def delete(self, request, ticketname):
        ticket = self.get_object(ticketname)
        ticket.delete()
        return Response('Ticket Deleted')
        


class ClientList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query == None:
            query = ''

        clients = Client.objects.filter(fullname__icontains=query)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


    def post(self, request):
        client = Client.objects.create(
            fullname=request.data['fullname'],
            email=request.data['email'],
            personal_id=request.data['personal_id'],
            company=request.data['company']
        )
        serializer = ClientSerializer(client, many=False)
        return Response(serializer.data)

    

class ClientDetails(APIView):
     

     def get_object(self, fullname):
        try:
            return Client.objects.get(fullname=fullname)
        except Client.DoesNotExisit:
            raise JsonResponse('Client Dosent Exist ! ')


     def get(self, request, fullname):
        client = self.get_object(fullname)
        serializer = ClientSerializer(client, many=False)
        return Response(serializer.data)

     def put(self, request, fullname):
        client = self.get_object(fullname)
        client.fullname = request.data['fullname']
        client.email = request.data['email']
        client.personal_id = request.data['personal_id']
        client.company = request.data['company']
        client.save()

        serializer = ClientSerializer(client, many=False)
        return Response(serializer.data)

     def delete(self, request, fullname):
        client = self.get_object(fullname)
        client.delete()
        return Response('Client Deleted')




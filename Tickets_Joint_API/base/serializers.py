from rest_framework.serializers import ModelSerializer
from .models import Ticket, Client


class TicektSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
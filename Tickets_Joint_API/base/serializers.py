from rest_framework.serializers import ModelSerializer
from .models import Ticket


class TicektSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
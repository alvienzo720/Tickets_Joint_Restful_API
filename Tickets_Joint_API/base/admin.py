from django.contrib import admin
from .models import Ticket, Client
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Client)
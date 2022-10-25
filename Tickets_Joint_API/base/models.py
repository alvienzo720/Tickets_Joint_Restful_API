from django.db import models

# Create your models here.

class Ticket(models.Model):
    ticket_name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_created=False, null=True)
    ticket_owner = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.ticket_name


class Client(models.Model):
    fullname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    personal_id = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.fullname + " , " + self.company


        


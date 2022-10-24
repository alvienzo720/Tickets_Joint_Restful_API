from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('tickets', views.ticket_list, name='tickets'),
    path('tickets/<str:ticketname>/', views.ticket_details),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    # path('tickets', views.ticket_list, name='tickets'),
    # path('tickets/<str:ticketname>/', views.ticket_details),
    path('tickets/<str:ticketname>/', views.TicketDetails.as_view()),
    path('tickets', views.TicketList.as_view()),
    path('clients', views.ClientList.as_view()),
    path('clients/<str:fullname>/', views.ClientDetails.as_view()),
   

    
]
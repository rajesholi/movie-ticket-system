from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    # MAIN BOOKING SYSTEM
    path('book/<int:movie_id>/', views.book_ticket, name='book_ticket'),

    # USER BOOKINGS
    path('my-bookings/', views.my_bookings, name='my_bookings'),

    # TICKET PAGE
    path('ticket/<int:booking_id>/', views.ticket, name='ticket'),
]
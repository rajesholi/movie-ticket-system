from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('book/<int:movie_id>/', views.book_ticket, name='book_ticket'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('ticket/<int:booking_id>/', views.ticket, name='ticket'),
]
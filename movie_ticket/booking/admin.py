from django.contrib import admin
from .models import Movie, Booking


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'ticket_price',
        'available_seats_count',
        'release_date'
    )

    search_fields = (
        'title',
    )

    list_filter = (
        'release_date',
    )

    def available_seats_count(self, obj):
        return obj.seat_set.filter(is_booked=False).count()

    available_seats_count.short_description = "Available Seats"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'movie',
        'quantity',
        'total_price',
        'booking_date'
    )

    search_fields = (
        'user__username',
        'movie__title'
    )

    list_filter = (
        'booking_date',
    )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Movie, Booking, Seat


# -------------------------
# AUTO SEATS
# -------------------------
def generate_seats(movie):

    rows = ['A', 'B', 'C']
    numbers = range(1, 11)

    for r in rows:
        for n in numbers:
            Seat.objects.get_or_create(
                movie=movie,
                number=f"{r}{n}"
            )


# -------------------------
# HOME
# -------------------------
def home(request):
    query = request.GET.get('q')

    movies = Movie.objects.filter(title__icontains=query) if query else Movie.objects.all()

    return render(request, 'home.html', {'movies': movies})


# -------------------------
# REGISTER (placeholder)
# -------------------------
def register(request):
    return render(request, 'register.html')


# -------------------------
# MY BOOKINGS
# -------------------------
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})


# -------------------------
# TICKET
# -------------------------
@login_required
def ticket(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'ticket.html', {'booking': booking})


# -------------------------
# BOOKING (MAIN FIXED)
# -------------------------
@login_required
def book_ticket(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)
    generate_seats(movie)

    seats = Seat.objects.filter(movie=movie)

    if request.method == "POST":

        selected_seats = request.POST.getlist("seats")

        if not selected_seats:
            return render(request, "seat_selection.html", {
                "movie": movie,
                "seats": seats,
                "error": "Please select seats"
            })

        with transaction.atomic():

            booking = Booking.objects.create(
                user=request.user,
                movie=movie,
                quantity=0,
                total_price=0
            )

            total = 0
            valid = 0

            for seat_id in selected_seats:

                seat = Seat.objects.filter(id=seat_id, movie=movie).first()

                if not seat or seat.is_booked:
                    continue

                seat.is_booked = True
                seat.save()

                booking.seats.add(seat)

                total += movie.ticket_price
                valid += 1

            if valid == 0:
                booking.delete()
                return render(request, "seat_selection.html", {
                    "movie": movie,
                    "seats": seats,
                    "error": "Seats already booked"
                })

            booking.quantity = valid
            booking.total_price = total
            booking.save()

            movie.available_seats = max(0, movie.available_seats - valid)
            movie.save()

        return redirect("ticket", booking.id)

    return render(request, "seat_selection.html", {
        "movie": movie,
        "seats": seats
    })
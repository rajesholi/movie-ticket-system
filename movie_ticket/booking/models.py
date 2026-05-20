from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    ticket_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available_seats = models.IntegerField(default=30)

    movie_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    number = models.CharField(max_length=10)  # A1, A2, B1...
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.movie.title} - Seat {self.number}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    seats = models.ManyToManyField(Seat)

    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
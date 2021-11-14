from django.db import models

from users.models import User


class Stadium(models.Model):
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Game(models.Model):
    class Status(models.TextChoices):
        TO_BE_PLAYED = "TO BE PLAYED"
        PLAYED = "PLAYED"
        CANCELLED = "CANCELLED"

    max_players = models.IntegerField(blank=False, null=False)
    date = models.DateTimeField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)

    stadium = models.ForeignKey(Stadium, on_delete=models.PROTECT)

    def __str__(self):
        return f"game: {self.stadium},{self.date}"

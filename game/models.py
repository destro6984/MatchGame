from django.db import models

from users.models import User


class Stadium(models.Model):
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.address}.{self.created_by.username}"


class Game(models.Model):
    class Status(models.TextChoices):
        TO_BE_PLAYED = "TO BE PLAYED"
        PLAYED = "PLAYED"
        CANCELLED = "CANCELLED"

    max_players = models.IntegerField(blank=False, null=False)
    game_date = models.DateTimeField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.ManyToManyField(
        User, related_name='games', blank=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.TO_BE_PLAYED)
    stadium = models.ForeignKey(Stadium, on_delete=models.PROTECT)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"game: {self.stadium},{self.game_date}"

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(blank=True, verbose_name="Opis")
    start_time = models.DateTimeField(verbose_name="Czas rozpoczęcia")
    end_time = models.DateTimeField(verbose_name="Czas zakończenia")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events", verbose_name="Użytkownik"
    )

    def __str__(self):
        return self.title
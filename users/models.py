from django.db import models

from cards.models import Card


class Deck(models.Model):
    name = models.CharField(max_length=30, unique=True)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.name

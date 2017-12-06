from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from cards.models import Card


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Deck(models.Model):
    name = models.CharField(max_length=30, unique=True)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.name

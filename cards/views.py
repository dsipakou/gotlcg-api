from rest_framework import generics

from cards.models import Card, Set
from .serializers import CardSerializer


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

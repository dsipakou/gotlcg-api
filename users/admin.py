from django.contrib import admin
from users.models import Deck


class DeckAdmin(admin.ModelAdmin):
    pass

admin.site.register(Deck, DeckAdmin)


from django.contrib import admin

from cards.models import Card, Trait, Challenge, Faction, Type, Set


class CardAdmin(admin.ModelAdmin):
    list_display = ('admin_image_tag', 'db_id', 'name', )


class TraitAdmin(admin.ModelAdmin):
    pass


class ChallengeAdmin(admin.ModelAdmin):
    pass


class FactionAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


class SetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Card, CardAdmin)
admin.site.register(Trait, TraitAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Set, SetAdmin)

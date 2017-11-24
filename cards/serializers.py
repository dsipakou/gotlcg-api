from rest_framework import serializers

from cards.models import Card, Trait


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ('name',)


class CardSerializer(serializers.ModelSerializer):
    set = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    faction = serializers.SerializerMethodField()
    traits = serializers.StringRelatedField(many=True)
    challenges = serializers.StringRelatedField(many=True)

    def get_set(self, card):
        return card.set.name

    def get_type(self, card):
        return card.type.name

    def get_faction(self, card):
        return card.faction.name

    class Meta:
        model = Card

        type = serializers.SlugRelatedField(
            many=False,
            read_only=True,
            slug_field='name', )
        traits = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field='name'
        )
        fields = (
            'db_id', 'name', 'set', 'type', 'faction', 'traits', 'gold', 'str', 'challenges', 'initiative', 'claim',
            'reserve', 'image_url')

from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Keyword(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Challenge(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Set(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Faction(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    db_id = models.CharField(max_length=6, unique=True)
    set = models.ForeignKey(Set)
    type = models.ForeignKey(Type)
    name = models.CharField(max_length=30)
    faction = models.ForeignKey(Faction)
    traits = models.ManyToManyField(Trait, blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    gold = models.IntegerField(blank=True)
    cost = models.IntegerField(blank=True)
    str = models.IntegerField(blank=True, default=0)
    challenges = models.ManyToManyField(Challenge, blank=True)
    initiative = models.IntegerField(blank=True, default=0)
    claim = models.IntegerField(blank=True, default=0)
    reserve = models.IntegerField(blank=True, default=0)
    image_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

    def admin_image_tag(self):
        return u'<img src="%s" style="max-width: 150px; max-height: 150px;"/>' % self.image_url

    admin_image_tag.allow_tags = True

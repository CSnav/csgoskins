from django.db import models

# Create your models here.

class GunSkin(models.Model):
    name = models.CharField(max_length=100)
    classid = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    weapon_type = models.CharField(max_length=20)
    gun_type = models.CharField(max_length=30)
    exterior = models.CharField(max_length=30)
    souvenir = models.BigIntegerField(default=0)
    tournament = models.CharField(max_length=100, default="")
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class GloveSkin(models.Model):
    name = models.CharField(max_length=100)
    classid = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class KnifeSkin(models.Model):
    name = models.CharField(max_length=100)
    classid = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    weapon_type = models.CharField(max_length=10)
    knife_type = models.CharField(max_length=20)
    # exterior = models.CharField(max_length=30)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)

    def __str__(self):
        return self.name




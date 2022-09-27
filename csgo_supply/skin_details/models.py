from django.db import models

# Create your models here.

class GunSkin(models.Model):
    name = models.CharField(max_length=300)
    icon_url = models.CharField(max_length=300, default="")
    icon_url_large = models.CharField(max_length=300, default="")
    weapon_type = models.CharField(max_length=20, default="")
    gun_type = models.CharField(max_length=30, default="")
    exterior = models.CharField(max_length=30)
    souvenir = models.BigIntegerField(default=0)
    stattrak = models.BigIntegerField(default=0)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)  
    class Meta:
        ordering = ['name'] 
    def __str__(self):
        return self.name

class GloveSkin(models.Model):
    name = models.CharField(max_length=300)
    icon_url = models.CharField(max_length=300)
    icon_url_large = models.CharField(max_length=300)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)
    exterior = models.CharField(max_length=30)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class KnifeSkin(models.Model):
    name = models.CharField(max_length=300)
    icon_url = models.CharField(max_length=300)
    icon_url_large = models.CharField(max_length=300)
    weapon_type = models.CharField(max_length=10)
    knife_type = models.CharField(max_length=20)
    exterior = models.CharField(max_length=30)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)
    stattrak = models.BigIntegerField(default=0)    
    class Meta:
        ordering = ['name'] 
    def __str__(self):
        return self.name

class SavedList(models.Model):
    guns = models.ManyToManyField(GunSkin, blank=True)
    knives = models.ManyToManyField(KnifeSkin, blank=True)
    gloves = models.ManyToManyField(GloveSkin, blank=True)

    def __str__(self):
        return str(self.pk)




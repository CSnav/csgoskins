from django.db import models
from .options import MODEL_EX_CHOICES, MODEL_GT_CHOICES, MODEL_WT_CHOICES, MODEL_KN_CHOICES

# Create your models here.


class GunSkin(models.Model):
    name = models.CharField(max_length=300)
    icon_url = models.CharField(max_length=300, default="")
    icon_url_large = models.CharField(max_length=300, default="")
    weapon_type = models.CharField(max_length=20, default="", choices=MODEL_WT_CHOICES)
    gun_type = models.CharField(max_length=30, default="", choices=MODEL_GT_CHOICES)
    exterior = models.CharField(max_length=30, choices=MODEL_EX_CHOICES)
    souvenir = models.BooleanField(default=False)
    stattrak = models.BooleanField(default=False)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)
    generic = models.CharField(max_length=30, default="", choices=MODEL_WT_CHOICES)   
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
    glove_type = models.CharField(max_length=40)
    generic = models.CharField(max_length=30, default="", choices=MODEL_WT_CHOICES)   
    exterior = models.CharField(max_length=30, choices=MODEL_EX_CHOICES)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class KnifeSkin(models.Model):
    name = models.CharField(max_length=300)
    icon_url = models.CharField(max_length=300)
    icon_url_large = models.CharField(max_length=300)
    weapon_type = models.CharField(max_length=10, choices=MODEL_WT_CHOICES)
    knife_type = models.CharField(max_length=20, choices=MODEL_KN_CHOICES)
    generic = models.CharField(max_length=30, default="", choices=MODEL_WT_CHOICES)   
    exterior = models.CharField(max_length=30, choices=MODEL_EX_CHOICES)
    rarity = models.CharField(max_length=20)
    rarity_color = models.CharField(max_length=10)
    stattrak = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['name'] 
    def __str__(self):
        return self.name

class SavedList(models.Model):
    guns = models.ManyToManyField(GunSkin, blank=True)
    knives = models.ManyToManyField(KnifeSkin, blank=True)
    gloves = models.ManyToManyField(GloveSkin, blank=True)
    name = models.CharField(max_length=100)

    @classmethod
    def init_list(cls):
        return cls()

    @classmethod
    def create_from_cookie(cls, cookies, name):
        skinlist = cls()
        skinlist.save()
        for category in cookies:
            for skin in cookies[category]:
                if (category == "Knife"):
                    print(f'\n\n\n\n\n {skin} \n\n\n\n\n')
                    skinlist.knives.add(KnifeSkin.objects.get(name=skin))
                elif (category == "Gloves"):
                    skinlist.gloves.add(GloveSkin.objects.get(name=skin))
                elif (category != 'csrf_token'):
                    skinlist.guns.add(GunSkin.objects.get(name=skin))
        skinlist.name = name
        return skinlist


    def __str__(self):
        return str(self.pk)




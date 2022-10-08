from django.db import models
from .options import MODEL_EX_CHOICES, MODEL_GT_CHOICES, MODEL_WT_CHOICES, MODEL_KN_CHOICES

# Create your models here.


#EX_CHOICES = [("Factory New", "Factory New"),
#              ("Minimal Wear", "Minimal Wear"),
#              ("Field-Tested", "Field-Tested"),
#              ("Well-Worn", "Well-Worn"),
#              ("Battle-Scarred", "Battle-Scarred")]
#GT_CHOICES = [("CZ75-Auto", "CZ75-Auto"), ("Desert Eagle", "Desert Eagle"), ("Dual Berettas", "Dual Berettas"),
#              ("Five-SeveN", "Five-SeveN"), ("Glock-18", "Glock-18"), ("P2000", "P2000"), ("P250", "P250"),
#              ("R8 Revolver", "R8 Revolver"), ("Tec-9", "Tec-9"), ("USP-S", "USP-S"), ("MAG-7", "MAG-7"),
#              ("Nova", "Nova"), ("Sawed-Off", "Sawed-Off"), ("XM1014", "XM1014"), ("M249", "M249"),
#              ("Negev", "Negev"), ("MAC-10", "MAC-10"), ("MP5-SD", "MP5-SD"), ("MP7", "MP7"), ("MP9", "MP9"),
#              ("P90", "P90"), ("PP-Bizon", "PP-Bizon"), ("UMP-45", "UMP-45"), ("AK-47", "AK-47"),
#              ("AUG", "AUG"), ("FAMAS", "FAMAS"), ("Galil AR", "Galil AR"), ("M4A1-S", "M4A1-S"),
#              ("M4A4", "M4A4"), ("SG 553", "SG 553"), ("AWP", "AWP"), ("G3SG1", "G3SG1"),
#              ("SCAR-20", "SCAR-20"), ("SSG 08", "SSG 08")]
#WT_CHOICES = [("Pistols", "Pistols"), ("Heavy", "Heavy"), ("Rifle", "Rifle"), ("SMG", "SMG"), ("Knife", "Knife")]


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

    @classmethod
    def init_list(cls):
        return cls()

    @classmethod
    def create_from_cookie(cls, cookies):
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
        return skinlist


    def __str__(self):
        return str(self.pk)




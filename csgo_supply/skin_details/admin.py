from django.contrib import admin
from .models import GunSkin, GloveSkin, KnifeSkin

# Register your models here.

admin.site.register(GunSkin)
admin.site.register(KnifeSkin)
admin.site.register(GloveSkin)
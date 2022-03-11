from django.shortcuts import render
from django.http import HttpResponse


skins = [
    {'type':'rifle', 'weapon':'ak47', 'finish':'Predator', 'fullname': 'AK-47 | Predator','listings':1},
    {'type':'rifle', 'weapon':'ak47', 'finish':'Jungle Spray', 'fullname': 'AK-47 | Jungle Spray','listings':2},
    {'type':'rifle', 'weapon':'ak47', 'finish':'Safari Mesh', 'fullname': 'AK-47 | Safari Mesh','listings':3},
    {'type':'rifle', 'weapon':'ak47', 'finish':'Baroque Purple', 'fullname': 'AK-47 | Baroque Purple','listings':4},
    {'type':'rifle', 'weapon':'ak47', 'finish':'Black Laminate', 'fullname': 'AK-47 | Black Laminate','listings':5},
    {'type':'rifle', 'weapon':'ak47', 'finish':'Green Laminate', 'fullname': 'AK-47 | Green Laminate','listings':6},
]

def home(request):
    context = {'skins': skins}
    return render(request, "skin_details/home.html", context)

def details(request, skinid):
    skin = None
    for i in skins:
        if i['fullname'] == skinid:
            skin = i
    context = {'skin':skin}
    return render(request, "skin_details/details.html",context)
# Create your views here.

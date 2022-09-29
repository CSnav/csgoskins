from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GunSkin, KnifeSkin, GloveSkin, SavedList
from .forms import ListForm
from django.core import serializers

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

def List(request, pk):
    skinlist = SavedList.objects.get(pk=pk)
    context = {'skinlist': skinlist}
    return render(request, "skin_details/list.html", context)

def CreateList(request):
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('list', pk=form.pk)
    context = {'form': form}
    return render(request, 'skin_details/list_form.html', context)
    
def gloveList(request):
    gloves = GloveSkin.objects.all() 
    context = {'gloves': gloves}
    return render(request, "skin_details/lists/gloveList.html", context)

def knifeList(request):
    knives = KnifeSkin.objects.all() 
    context = {'knives': knives}
    return render(request, "skin_details/lists/knifeList.html", context)

def gunList(request):
    guns = GunSkin.objects.all() 
    context = {'guns': guns}
    return render(request, "skin_details/lists/gunList.html", context)

def gunDetails(request, skinid):
    gun = GunSkin.objects.get(name=skinid)
    context = {'gun':gun}
    return render(request, "skin_details/details/gunDetails.html",context)

def knifeDetails(request, skinid):
    knife = KnifeSkin.objects.get(name=skinid)
    context = {'knife':knife}
    return render(request, "skin_details/details/knifeDetails.html",context)

def gloveDetails(request, skinid):
    glove = GloveSkin.objects.get(name=skinid)
    context = {'glove':glove}
    return render(request, "skin_details/details/gloveDetails.html",context)
# Create your views here.

def JsonList(request):
    data = serializers.serialize('json',SavedList.objects.all())
    return HttpResponse(data, content_type='application/json')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GunSkin, KnifeSkin, GloveSkin, SavedList
from .forms import ListForm, GunExteriorFilterForm
from django.core import serializers
from django.core.paginator import Paginator
from .options import EX_CHOICES, KN_CHOICES, WT_CHOICES, GT_CHOICES, GL_CHOICES
from django.db.models import Q
import json

def home(request):
    return render(request, "skin_details/home.html")


def List(request, pk):
    skinlist = SavedList.objects.get(pk=pk)
    # context = {'skinlist': skinlist}
    # return render(request, "skin_details/list.html", context)
    categories = {
                    'Rifle': [],
                    'SMG': [],
                    'Heavy': [],
                    'Pistol': [],
                    'Knife': [],
                    'Gloves': []
                }
    for gun in skinlist.guns.all():
        categories[gun.generic].append(gun)
    for knife in skinlist.knives.all():
        categories[knife.generic].append(knife)
    for gloves in skinlist.gloves.all():
        categories[gloves.generic].append(gloves)
    context = {'categories': categories}
    return render(request, 'skin_details/list.html', context)

def CreateList(request):
    guns = []
    gloves = []
    knives = []
    categories = {
                    'Rifle': [],
                    'SMG': [],
                    'Heavy': [],
                    'Pistol': [],
                    'Knife': [],
                    'Gloves': []
                }
    for key in categories:
        temp = json.loads(request.COOKIES.get(key, "[]"))
        for name in temp:
            if(key == "Gloves"):
                categories[key].append(GloveSkin.objects.get(name=name))
            elif(key == "Knife"):
                categories[key].append(KnifeSkin.objects.get(name=name))
            elif(key != "csrf_token"):
                categories[key].append(GunSkin.objects.get(name=name))
    form = ListForm()
    if request.method == 'POST':
        skinlist = SavedList.init_list() 
        skinlist.save()
        for key in categories:
            for skin in categories[key]:
                if(key == "Knife"):
                    skinlist.knives.add(skin)
                elif(key == "Gloves"):
                    skinlist.gloves.add(skin)
                else:
                    skinlist.guns.add(skin)
        skinlist.save()
        print("skinlist:         ", skinlist)
        direct = redirect('list', pk=skinlist.pk)
        for i in categories:
            direct.delete_cookie(i)
        return direct 
    print(categories)
    context = {'categories': categories}
    return render(request, 'skin_details/list_form.html', context)


def gloveList(request):
    params = {
              'exterior': request.GET.getlist('exterior') or None,
              'glove_type': request.GET.getlist('glove_type') or None,
             }
    andlist = []
    for param in params:
        if params[param]:
            andlist.append(Q())
            for field in params[param]:
                if(param == "glove_type"):
                    andlist[-1] |= Q(glove_type=field)
                if(param == "exterior"):
                    andlist[-1] |= Q(exterior=field)
    if(andlist):
        gloves = GloveSkin.objects.filter(*andlist)
    else:
        gloves = GloveSkin.objects.all()
    paginator = Paginator(gloves, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    filter_options = {'exterior': EX_CHOICES,
                      'glove_type': GL_CHOICES, }
    return render(
         request, 'skin_details/lists/gloveList.html',
         {'page_obj': page_obj, 'filters': filter_options})


def knifeList(request):
    params = {'knife_type': request.GET.getlist('knife_type') or None,
              'exterior': request.GET.getlist('exterior') or None,
              'stattrak': request.GET.getlist('stattrak') or None,
             }
    andlist = []
    for param in params:
        if params[param]:
            andlist.append(Q())
            for field in params[param]:
                if(param == "knife_type"):
                    andlist[-1] |= Q(knife_type=field)
                elif(param == "exterior"):
                    andlist[-1] |= Q(exterior=field)
                elif(param == "stattrak"):
                    andlist[-1] |= Q(stattrak=field)
    if(andlist):
        knives = KnifeSkin.objects.filter(*andlist)
    else:
        knives = KnifeSkin.objects.all()
    paginator = Paginator(knives, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    filter_options = {'exterior': EX_CHOICES,
                      'knife_type': KN_CHOICES,
                      'stattrak': [True, False]}
    return render(
         request, 'skin_details/lists/knifeList.html',
         {'page_obj': page_obj, 'filters': filter_options})

def gunList(request):
    params = {'gun_type': request.GET.getlist('gun_type') or None,
              'exterior': request.GET.getlist('exterior') or None,
              'souvenir': request.GET.getlist('souvenir') or None,
              'weapon_type': request.GET.getlist('weapon_type') or None,
              'stattrak': request.GET.getlist('stattrak') or None,
             }
    andlist = []
    print("cookie: ", json.loads(request.COOKIES.get('Rifle', "[]")))
    for param in params:
        if params[param]:
            andlist.append(Q())
            for field in params[param]:
                if(param == "gun_type"):
                    andlist[-1] |= Q(gun_type=field)
                elif(param == "exterior"):
                    andlist[-1] |= Q(exterior=field)
                elif(param == "souvenir"):
                    andlist[-1] |= Q(souvenir=field)
                elif(param == "stattrak"):
                    andlist[-1] |= Q(stattrak=field)
                elif(param == "weapon_type"):
                    andlist[-1] |= Q(weapon_type=field)
    print(andlist) 
    if(andlist):
        guns = GunSkin.objects.filter(*andlist)
    else:
        guns = GunSkin.objects.all()
    paginator = Paginator(guns, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    filter_options = {'exterior': EX_CHOICES,
                      'gun_type': GT_CHOICES,
                      'weapon_type': WT_CHOICES,
                      'souvenir': [True, False],
                      'stattrak': [True, False]}
    return render(
         request, 'skin_details/lists/gunList.html',
         {'page_obj': page_obj, 'filters': filter_options})


def gunDetails(request, skinid):
    gun = GunSkin.objects.get(name=skinid)
    context = {'gun': gun}
    return render(request, "skin_details/details/gunDetails.html", context)


def knifeDetails(request, skinid):
    knife = KnifeSkin.objects.get(name=skinid)
    context = {'knife': knife}
    return render(request, "skin_details/details/knifeDetails.html", context)


def gloveDetails(request, skinid):
    glove = GloveSkin.objects.get(name=skinid)
    context = {'glove': glove}
    return render(request, "skin_details/details/gloveDetails.html", context)


def JsonList(request):
    data = serializers.serialize('json', SavedList.objects.all())
    return HttpResponse(data, content_type='application/json')

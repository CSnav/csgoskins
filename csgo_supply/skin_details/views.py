from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GunSkin, KnifeSkin, GloveSkin, SavedList
from .forms import ListForm, GunExteriorFilterForm
from django.core import serializers
from django.core.paginator import Paginator


def home(request):
    return render(request, "skin_details/home.html")


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
    params = {'gun_type': request.GET.get('gun_type') or None,
              'exterior': request.GET.get('exterior') or None,
              'souvenir': request.GET.get('souvenir') or None,
              'weapon_type': request.GET.get('weapon_type') or None,
              'stattrak': request.GET.get('stattrak') or None,
              'rarity': request.GET.get('rarity') or None}
    filtered_params = {}
    for key in params:
        if(params[key]):
            filtered_params[key] = params[key]
    if(filtered_params):
        guns = GunSkin.objects.filter(**filtered_params)
    else:
        guns = GunSkin.objects.all()
    paginator = Paginator(guns, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = GunExteriorFilterForm()
    return render(
         request, 'skin_details/lists/gunList.html',
         {'form': form, 'page_obj': page_obj, })
    return render(request, 'skin_details/lists/gunList.html', {'page_obj': page_obj})


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

from django.shortcuts import render
from django.http import HttpResponse




def details(request):
    return render(request, "details.html")
# Create your views here.

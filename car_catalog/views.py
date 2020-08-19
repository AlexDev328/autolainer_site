from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import Car
# Create your views here.


def home(request):
    return render(request, "home.html")


def catalog(request):
    context = {'cars': Car.objects.all}
    return render(request, "catalog.html", context=context)


def feedback(request):
    return HttpResponseNotFound("Страница ещё не готова")
from django.db.models import Q
from django.http import request
from django.shortcuts import redirect, render
# from django.views.generic import CreateView, ListView, TemplateView, FormView
from django.urls import reverse_lazy, reverse
from app_Cars.models import Car
from .forms import CarsFilterForms


# class CarList(ListView):
#     model = Car
#     # form= CarsFilterForms(request.GET)
#     template_name = 'index.html'

def cars_view(request):
    cars=Car.objects.all()
    form = CarsFilterForms(request.GET)
    if form.is_valid():
        # if form.cleaned_data["search"]:
        #     cars= Car.objects.filter(Q(manufacturer__contains = form.cleaned_data["search"])|Q(modelCar__contains = form.cleaned_data["search"]))
        # elif form.cleaned_data["search"] and  form.cleaned_data["search_year"] :
        #     cars1 = Car.objects.filter(Q(manufacturer__contains=form.cleaned_data["search"]) | Q(modelCar__contains=form.cleaned_data["search"]))
        #     cars=cars1.filter(Q(year_manufacture__gt=form.cleaned_data["search_year"]))
        # # elif form.cleaned_data["search_transmission"]:
        #     cars = Car.objects.filter(Q(transmission__contains=form.cleaned_data["search_transmission"]))
        #
        # else:
        #     cars = Car.objects.all()
        if form.cleaned_data["search"]:
            cars= Car.objects.filter(Q(manufacturer__contains = form.cleaned_data["search"])|Q(modelCar__contains = form.cleaned_data["search"]))
        if form.cleaned_data["search_year"]:
            cars=cars.filter(year_manufacture__gt=form.cleaned_data["search_year"])
        if form.cleaned_data["search_transmission"]:
            cars = Car.objects.filter(Q(transmission__contains=form.cleaned_data["search_transmission"]))




    context={"cars":cars, "form":form}
    return render(request,'index.html', context)
# search_year
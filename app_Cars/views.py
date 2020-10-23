from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, TemplateView, FormView
from django.urls import reverse_lazy, reverse
from app_Cars.models import Car


class CarList(ListView):
    model = Car
    template_name = 'index.html'
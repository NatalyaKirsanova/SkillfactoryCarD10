from django.urls import path
from .views import CarList

app_name = 'app_Cars'

urlpatterns = [
    path('', CarList.as_view(template_name='index.html'), name='index'),
]
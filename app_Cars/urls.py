from django.urls import path
# from .views import CarList,cars_view
from .views import cars_view

app_name = 'app_Cars'

urlpatterns = [
    path('', cars_view, name='index'),
    # path('', CarList.as_view(template_name='index.html'), name='index'),
]
from django import forms


class CarsFilterForms(forms.Form):
    search=forms.CharField(label='производитель/модель',required=False)
    search_year = forms.IntegerField(label='год выпуска больше', required=False)
    # search_transmission =forms.CharField(label='коробка передач', required=False)
    # transmission
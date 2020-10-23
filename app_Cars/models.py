from django.db import models
from django.utils.translation import gettext as _
from colorfield.fields import ColorField

# Create your models here.
class Car(models.Model):
    TRANSMISSION_CHOICES = (
        (0, ''),
        (1, 'mechanics'),
        (2, 'automatic'),
        (3, 'robot'),
    )
    manufacturer = models.CharField(max_length=256, verbose_name = _("Производитель"))
    modelCar = models.CharField(max_length=128, verbose_name = _("Модель"))
    year_manufacture = models.IntegerField(verbose_name = _("Год выпуска"))
    transmission=models.SmallIntegerField(default=0, choices=TRANSMISSION_CHOICES, verbose_name =_("Коробка передачи"))
    # colormodel=models.CharField(max_lenght=256)
    color = ColorField( default='#FF0000' )

    def __str__(self):
        return self.manufacturer

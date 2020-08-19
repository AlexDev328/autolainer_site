from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    main_photo = models.ImageField()
    description = models.TextField(verbose_name="Описание")





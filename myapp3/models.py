from time import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CarName(models.Model):
    """Название Компании производителя машин"""
    name = models.CharField("Name", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car label"
        verbose_name_plural = "Cars label"

class Genre(models.Model):
    """Марка автомобиля"""
    name = models.CharField("Имя", max_length=100)
    category = models.ForeignKey(CarName, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"


class Specifications(models.Model):
    """Характеристика типа топлива"""
    fuel_type = models.CharField("Тип топлива", max_length=100)

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = "Топливо"
        verbose_name_plural = "Топливо"

class Category(models.Model):
    """Категории транспортных средств"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория ТС"
        verbose_name_plural = "Категории ТС"

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Car(models.Model):
    """Объявления автомобилей"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец машины", blank=True, null=True)
    title = models.ForeignKey(CarName, verbose_name="Cars", on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre,  max_length=100)
    category = models.ManyToManyField(Category,  max_length=100)
    fuel = models.ManyToManyField(Specifications,  max_length=100)
    poster = models.ImageField("Фото", null=True, default=None, upload_to="movies/")
    price = models.PositiveIntegerField("Цена", default=0, help_text="указывать сумму в долларах")
    slug = models.SlugField("Url", max_length=150, blank=True, unique=False)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title.name

    def get_absolute_url(self):
        return reverse("car_detail_url", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

class CarShorts(models.Model):
    image = models.ImageField("Pictures", upload_to="movie_shots/")
    car = models.ForeignKey(Car, verbose_name="Car", on_delete=models.CASCADE)

    def __str__(self):
        return self.car.title.name

    class Meta:
        verbose_name = "Short"
        verbose_name_plural = "Shorts"


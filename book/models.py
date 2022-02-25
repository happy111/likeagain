from django.db import models
from product.models import Common


# Create your models here.

class Publisher(Common):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    active_status = models.BooleanField(
        default=True)

    def __str__(self):
        return self.name


class Book(Common):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Store(Common):
    name = models.CharField(
        max_length=255
    )
    book = models.ManyToManyField(
        Book
    )

    def __str__(self):
        return self.name

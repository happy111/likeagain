from django.db import models


class Common(models.Model):
    active_status = models.BooleanField(
        default=True)
    created_at = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.  ctrl+alt+l
class Category(Common):
    name = models.CharField(max_length=250,
                            blank=True,
                            null=True)
    created_at = None

    def __str__(self):
        return self.name

    def display(self):
        return "umesh"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)
    product_name = models.CharField(
        max_length=200
    )
    price = models.FloatField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.product_name

from django.db import models

# Create your models here.


class Category(models.Model):
	category_name = models.CharField(max_length=255)
	code = models.CharField(max_length=233)

	def __str__(self):
		return self.category_name


class Productcategory(models.Model):
	category_name = models.ForeignKey(Category,
		related_name='Productcategory_category_name',
		on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=233)
	price = models.FloatField(
		blank=True,
        null=True)

	def __str__(self):
		return self.name
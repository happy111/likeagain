from django.http import HttpResponse
from product.models import Category


def category(request):
	obj = Category.objects.all()
	obj1 = Category()
	print("ssssssssssssssss", obj1.display())
	return HttpResponse("Hi")


def excp(request):
	print("I am exception")
	a = 10 / 0
	return HttpResponse("Hi")

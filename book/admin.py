from django.contrib import admin
from book.models import *

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)

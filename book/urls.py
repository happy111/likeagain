from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book),
    path('orm/', views.orm)

]

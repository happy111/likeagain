from django.test import TestCase
from .models import Animals

class AnimalTestCase(TestCase):
    def setUp(self):
        Animals.objects.create(name="lion", place="roar")
        Animals.objects.create(name="cat", place="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animals.objects.get(name="lion")
        cat = Animals.objects.get(name="cat")

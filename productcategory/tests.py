from django.test import TestCase

# Create your tests here.
from datetime import datetime

class Message:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
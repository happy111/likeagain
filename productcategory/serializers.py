from django.db.models import fields
from rest_framework import serializers
from .models import *


class ProductcateggorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Productcategory
       # fields = "__all__"
        fields = ['name']


class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
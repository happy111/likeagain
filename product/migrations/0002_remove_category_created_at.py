# Generated by Django 3.2.11 on 2022-01-14 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]

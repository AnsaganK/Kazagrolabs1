# Generated by Django 3.1.4 on 2020-12-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0009_auto_20201215_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementsname',
            name='basic',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-22 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0016_auto_20201222_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcorm',
            name='count',
        ),
    ]
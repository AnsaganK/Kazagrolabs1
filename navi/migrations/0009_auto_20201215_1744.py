# Generated by Django 3.1.4 on 2020-12-15 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0008_auto_20201215_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='User',
            new_name='user',
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-11 07:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('countSamples', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='elementsName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Элемент',
                'verbose_name_plural': 'Элементы',
            },
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='navi.client')),
                ('elements', models.ManyToManyField(related_name='elements', to='navi.elementsName')),
            ],
            options={
                'verbose_name': 'Проба',
                'verbose_name_plural': 'Пробы',
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countSamples', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('nowTime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 11, 13, 41, 49, 333862), null=True)),
                ('status', models.CharField(choices=[('Поступило', 'Поступило'), ('В процессе', 'В процессе'), ('Готово', 'Готово')], default='Поступило', max_length=200)),
                ('nameClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.client')),
                ('samples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.samples')),
            ],
            options={
                'verbose_name': 'Почвоотбор',
                'verbose_name_plural': 'Почвоотбор',
            },
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countSamples', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('nowTime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 11, 13, 41, 49, 333862), null=True)),
                ('status', models.CharField(choices=[('Поступило', 'Поступило'), ('В процессе', 'В процессе'), ('Готово', 'Готово')], default='Поступило', max_length=200)),
                ('nameClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.client')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='navi.selection')),
                ('samples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.samples')),
            ],
            options={
                'verbose_name': 'Пробоподготовка',
                'verbose_name_plural': 'Пробоподготовка',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countSamples', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('nowTime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 11, 13, 41, 49, 334860), null=True)),
                ('status', models.CharField(choices=[('Поступило', 'Поступило'), ('В процессе', 'В процессе'), ('Готово', 'Готово')], default='Поступило', max_length=200)),
                ('nameClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.client')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='navi.preparation')),
                ('samples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.samples')),
            ],
            options={
                'verbose_name': 'Лаборатория',
                'verbose_name_plural': 'Лаборатория',
            },
        ),
        migrations.CreateModel(
            name='Agrohym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countSamples', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('nowTime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 11, 13, 41, 49, 334860), null=True)),
                ('status', models.CharField(choices=[('Поступило', 'Поступило'), ('В процессе', 'В процессе'), ('Готово', 'Готово')], default='Поступило', max_length=200)),
                ('nameClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.client')),
                ('samples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navi.samples')),
            ],
            options={
                'verbose_name': 'Агрохим',
                'verbose_name_plural': 'Агрохим',
            },
        ),
    ]

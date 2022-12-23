# Generated by Django 4.1.3 on 2022-12-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100, verbose_name='ФИО покупателя')),
                ('tarif', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тариф')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]

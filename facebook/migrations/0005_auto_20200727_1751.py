# Generated by Django 3.0.8 on 2020-07-27 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_productfb_modal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productfb',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
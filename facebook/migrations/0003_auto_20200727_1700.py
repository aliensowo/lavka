# Generated by Django 3.0.8 on 2020-07-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_productfb_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriesproducts',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='productfb',
            old_name='Count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='productfb',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productfb',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productfb',
            old_name='Price',
            new_name='price',
        ),
    ]

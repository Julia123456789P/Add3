# Generated by Django 4.1.1 on 2022-10-06 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unloaded',
            new_name='uploaded',
        ),
    ]

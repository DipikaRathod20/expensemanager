# Generated by Django 5.0.2 on 2024-02-27 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='SubCategory',
            new_name='subcategory',
        ),
    ]
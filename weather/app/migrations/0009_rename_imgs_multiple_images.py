# Generated by Django 4.1.4 on 2023-02-16 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_multiple'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiple',
            old_name='imgs',
            new_name='images',
        ),
    ]
# Generated by Django 4.1.4 on 2023-02-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default=12, upload_to='images/'),
            preserve_default=False,
        ),
    ]

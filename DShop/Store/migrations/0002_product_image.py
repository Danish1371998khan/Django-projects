# Generated by Django 3.1.2 on 2020-10-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='com/danish/'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-10-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_with_recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo_of_the_dish',
            field=models.FileField(upload_to='my_gallery'),
        ),
    ]

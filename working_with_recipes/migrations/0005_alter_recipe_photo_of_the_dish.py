# Generated by Django 4.2.3 on 2023-10-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_with_recipes', '0004_alter_recipe_autor_alter_recipe_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo_of_the_dish',
            field=models.FileField(upload_to='my_gallery'),
        ),
    ]

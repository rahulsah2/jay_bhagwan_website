# Generated by Django 5.1.1 on 2024-09-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_remove_category_parent_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="static/images/"),
        ),
    ]

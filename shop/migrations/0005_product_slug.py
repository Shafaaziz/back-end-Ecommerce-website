# Generated by Django 4.2 on 2024-03-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_slug_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]

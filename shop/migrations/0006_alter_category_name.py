# Generated by Django 4.2 on 2024-03-31 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='نام'),
        ),
    ]
# Generated by Django 4.2 on 2024-04-13 06:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_imagegallery_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='جزئیات محصول'),
        ),
    ]
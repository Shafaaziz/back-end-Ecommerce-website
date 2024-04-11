# Generated by Django 4.2 on 2024-04-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_imagegallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نطر', 'verbose_name_plural': 'نظرها'},
        ),
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'verbose_name': 'گالری عکس\u200cها', 'verbose_name_plural': 'گالری عکس\u200cها'},
        ),
        migrations.AddField(
            model_name='imagegallery',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

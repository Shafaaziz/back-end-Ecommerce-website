# Generated by Django 4.2 on 2024-03-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصولات', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='تعداد'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='موجودی'),
        ),
    ]
# Generated by Django 4.2 on 2024-04-07 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_product_like_alter_product_unlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='size_variant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.size', verbose_name='سایز'),
        ),
    ]
# Generated by Django 4.2 on 2024-03-31 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_first'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربرها'},
        ),
    ]
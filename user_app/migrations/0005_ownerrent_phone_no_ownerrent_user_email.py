# Generated by Django 4.1.7 on 2023-03-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_rename_division_sell_land_divission'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerrent',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ownerrent',
            name='user_email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
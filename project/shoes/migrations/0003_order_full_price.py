# Generated by Django 4.2.6 on 2023-11-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='full_price',
            field=models.PositiveBigIntegerField(default=0, verbose_name='قیمت کل سفارش'),
        ),
    ]
# Generated by Django 2.1.4 on 2019-02-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0002_auto_20190204_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='deliveryHour',
            field=models.TimeField(verbose_name='Conversation Time'),
        ),
    ]

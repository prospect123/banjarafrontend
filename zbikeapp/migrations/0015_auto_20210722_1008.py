# Generated by Django 3.2.4 on 2021-07-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0014_auto_20210722_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='fuel_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='kilometer',
            field=models.IntegerField(null=True),
        ),
    ]

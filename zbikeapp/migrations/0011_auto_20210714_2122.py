# Generated by Django 3.2.4 on 2021-07-14 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0010_auto_20210714_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='Pricefilter',
        ),
        migrations.DeleteModel(
            name='Priceselector',
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0018_auto_20210725_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='registration_No',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0011_auto_20210714_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='Date_of_add',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='Video',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='car_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='fuel_type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='image2',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image3',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image4',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image5',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image6',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image7',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image8',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='image9',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='kilometer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='model',
            field=models.TextField(null=True),
        ),
    ]

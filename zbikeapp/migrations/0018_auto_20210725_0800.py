# Generated by Django 3.2.4 on 2021-07-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0017_cars_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='fuel_type',
            field=models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel')], default='petrol', max_length=30),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image7',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image8',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image9',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
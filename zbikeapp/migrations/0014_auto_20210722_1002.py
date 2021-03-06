# Generated by Django 3.2.4 on 2021-07-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0013_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='car_number',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='discription',
        ),
        migrations.AddField(
            model_name='cars',
            name='Insurance',
            field=models.CharField(choices=[('comprehensive', 'comprehensive'), ('third_party', 'third_party'), ('expired', 'expired')], default='comprehensive', max_length=30),
        ),
        migrations.AddField(
            model_name='cars',
            name='colour_family',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='owners',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('more_than_4', 'more_than_4')], default='1', max_length=30),
        ),
        migrations.AddField(
            model_name='cars',
            name='registration_No',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='registration_type',
            field=models.CharField(choices=[('unregistred', 'unregistred'), ('Individual', 'Individual'), ('Corporate', 'Corporate'), ('Taxi', 'Taxi'), ('commercial_registration', 'commercial_registration')], default='Individual', max_length=30),
        ),
        migrations.AlterField(
            model_name='cars',
            name='model',
            field=models.IntegerField(null=True),
        ),
    ]

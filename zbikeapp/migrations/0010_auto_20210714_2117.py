# Generated by Django 3.2.4 on 2021-07-14 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0009_cli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priceselector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='Pricefilter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zbikeapp.priceselector'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-06 19:45

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PAYMENT_PROCEDUREs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PRIVACY_POLICYs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TERMS_CONDITIONSs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
    ]

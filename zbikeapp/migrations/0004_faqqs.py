# Generated by Django 3.2.4 on 2021-07-06 20:07

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0003_booking_tips'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQQS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
    ]
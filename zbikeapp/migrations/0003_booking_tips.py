# Generated by Django 3.2.4 on 2021-07-06 19:46

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0002_payment_procedures_privacy_policys_terms_conditionss'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKING_TIPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
    ]
# Generated by Django 3.2.4 on 2021-07-09 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zbikeapp', '0006_carcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='cars',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zbikeapp.carcategory'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-07 18:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='caption',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
        ),
    ]
# Generated by Django 2.2.12 on 2020-04-01 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickevent',
            name='kirr_url',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shortener.KirrURL'),
        ),
    ]

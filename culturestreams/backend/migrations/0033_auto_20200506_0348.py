# Generated by Django 3.0.4 on 2020-05-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_auto_20200505_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1500, verbose_name='Beschreibung'),
        ),
    ]

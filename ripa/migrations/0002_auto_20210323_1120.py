# Generated by Django 3.1.7 on 2021-03-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ripa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='datetime_closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ripa', '0006_auto_20210323_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionUnderTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10)),
            ],
        ),
    ]

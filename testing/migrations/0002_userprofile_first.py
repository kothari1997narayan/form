# Generated by Django 2.2.7 on 2019-12-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

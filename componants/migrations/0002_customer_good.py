# Generated by Django 2.1 on 2019-02-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='good',
            field=models.NullBooleanField(),
        ),
    ]

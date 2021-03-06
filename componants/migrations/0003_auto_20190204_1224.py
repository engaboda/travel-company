# Generated by Django 2.1 on 2019-02-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componants', '0002_customer_good'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='good',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='holidays',
            field=models.CharField(choices=[('thu-fri', 'Friday and Thursday'), ('fri-sat', 'Friday and Satrday')], max_length=7),
        ),
    ]

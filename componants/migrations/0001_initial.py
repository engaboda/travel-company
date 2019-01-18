# Generated by Django 2.1 on 2019-01-18 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owenr', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('job', models.CharField(max_length=100)),
                ('factory', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('holidays', models.CharField(choices=[('thu-fri', 'Friday and Thursday'), ('fri-sat', 'Friday and Satrday')], max_length=7)),
                ('dependacy', models.IntegerField()),
                ('joined_day', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('salary', models.IntegerField()),
                ('promo', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_salary', to='componants.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_place', models.CharField(max_length=100)),
                ('t_place', models.CharField(max_length=100)),
                ('esti_time', models.TimeField()),
                ('gas', models.DecimalField(decimal_places=3, max_digits=100)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel_bus', to='componants.Bus')),
                ('customer', models.ManyToManyField(related_name='customers_travel', to='componants.Customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_travel', to='componants.Driver')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='Driver',
            field=models.ManyToManyField(related_name='driver_bus', to='componants.Driver'),
        ),
    ]

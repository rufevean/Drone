# Generated by Django 4.0.4 on 2023-04-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('carrying_capacity', models.FloatField()),
                ('flight_time', models.FloatField()),
                ('max_speed', models.FloatField()),
                ('weight', models.FloatField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

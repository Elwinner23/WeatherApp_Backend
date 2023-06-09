# Generated by Django 4.1.7 on 2023-04-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0005_alter_continent_continent_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conutry_name', models.CharField(max_length=30, unique=True)),
                ('flag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DateWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weather_status', models.CharField(max_length=255)),
                ('status_icon', models.TextField()),
                ('wind_speed', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.city')),
            ],
        ),
        migrations.AddField(
            model_name='continent',
            name='continent_img',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
        migrations.AddField(
            model_name='country',
            name='conitnent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.continent'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.country'),
        ),
    ]

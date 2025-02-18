# Generated by Django 5.0.4 on 2024-04-13 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_type', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Night', 'Night')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='dutyschedule',
            name='doctor_name',
        ),
        migrations.AlterField(
            model_name='dutyschedule',
            name='day',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='dutyschedule',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.doctor'),
        ),
        migrations.AlterField(
            model_name='dutyschedule',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shift'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=20),
        ),
    ]
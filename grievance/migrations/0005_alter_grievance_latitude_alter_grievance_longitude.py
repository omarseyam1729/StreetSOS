# Generated by Django 5.0.6 on 2024-09-11 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0004_alter_grievance_latitude_alter_grievance_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='latitude',
            field=models.DecimalField(decimal_places=14, max_digits=40),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='longitude',
            field=models.DecimalField(decimal_places=14, max_digits=40),
        ),
    ]

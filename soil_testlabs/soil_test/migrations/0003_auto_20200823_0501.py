# Generated by Django 3.0.6 on 2020-08-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soil_test', '0002_remove_state_state_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
    ]

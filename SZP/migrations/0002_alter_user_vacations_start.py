# Generated by Django 3.2.5 on 2021-07-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SZP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vacations_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
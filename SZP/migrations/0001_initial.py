# Generated by Django 3.2.5 on 2021-07-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('vacations_start', models.DateField(null=True)),
                ('vacations_end', models.DateField(null=True)),
                ('sick_leave', models.BooleanField(default=False)),
            ],
        ),
    ]

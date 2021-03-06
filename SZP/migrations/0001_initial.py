# Generated by Django 3.2.5 on 2021-07-08 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CastingMold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=128)),
                ('owner', models.CharField(max_length=128)),
                ('tool_shop', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('vendor', models.CharField(max_length=128)),
                ('serial_number', models.CharField(max_length=128)),
                ('power_consumption', models.IntegerField()),
                ('type', models.IntegerField(choices=[(0, 'odlewnicza'), (1, 'wózek widłowy'), (2, 'CNC')], default=-1)),
                ('orientation', models.IntegerField(choices=[(0, 'horyzontalna'), (1, 'wertykalna')], default=-1)),
                ('pressure', models.IntegerField()),
                ('pressure_tank', models.IntegerField()),
                ('technological_schema', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('type', models.IntegerField(choices=[(0, 'hydroakumulator'), (1, 'akumulator tłokowy')], default=-1)),
                ('max_pressure', models.IntegerField()),
                ('work_pressure', models.IntegerField()),
                ('valve_setting_pressure', models.IntegerField()),
                ('serial_number', models.CharField(max_length=128)),
                ('UDT_number', models.CharField(max_length=128)),
                ('UDT_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_name', models.CharField(max_length=128)),
                ('alloy_type', models.IntegerField(choices=[(0, '226'), (1, '231'), (2, '230'), (3, 'ZL5')], default=-1)),
                ('pdf_file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('casting_mold', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SZP.castingmold')),
                ('machine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SZP.machines')),
            ],
        ),
        migrations.AddField(
            model_name='machines',
            name='tank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SZP.tank'),
        ),
        migrations.CreateModel(
            name='Furnace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('power_source', models.IntegerField(choices=[(0, 'gaz'), (1, 'prąd')], default=-1)),
                ('machine', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='SZP.machines')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=64)),
                ('vacations_start', models.DateField(blank=True, null=True)),
                ('vacations_end', models.DateField(blank=True, null=True)),
                ('sick_leave', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='castingmold',
            name='machines',
            field=models.ManyToManyField(through='SZP.TechSchema', to='SZP.Machines'),
        ),
    ]

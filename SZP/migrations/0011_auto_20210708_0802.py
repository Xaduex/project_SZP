# Generated by Django 3.2.5 on 2021-07-08 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SZP', '0010_auto_20210705_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='castingmold',
            name='Machines',
        ),
        migrations.RemoveField(
            model_name='tank',
            name='machine',
        ),
        migrations.AddField(
            model_name='castingmold',
            name='machines',
            field=models.ManyToManyField(through='SZP.TechSchema', to='SZP.Machines'),
        ),
        migrations.AddField(
            model_name='machines',
            name='tank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SZP.tank'),
        ),
    ]
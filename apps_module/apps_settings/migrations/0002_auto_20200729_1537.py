# Generated by Django 3.0.7 on 2020-07-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='position',
        ),
        migrations.AddField(
            model_name='position',
            name='position_name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(default='Admin', max_length=20),
        ),
    ]

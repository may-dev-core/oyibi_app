# Generated by Django 3.0.7 on 2020-07-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_settings', '0003_auto_20200729_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]

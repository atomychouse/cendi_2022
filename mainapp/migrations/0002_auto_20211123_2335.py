# Generated by Django 2.2 on 2021-11-23 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='date_history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='sintoms',
            field=models.TextField(blank=True, null=True),
        ),
    ]

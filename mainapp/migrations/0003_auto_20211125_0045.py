# Generated by Django 2.2 on 2021-11-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211123_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='last_names',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2 on 2022-06-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]

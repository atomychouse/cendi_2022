# Generated by Django 2.2 on 2022-06-29 20:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20220629_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='fin',
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='inicio',
        ),
        migrations.AddField(
            model_name='cuota',
            name='aplica',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuota',
            name='monto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='recargo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='HistorialPago',
        ),
        migrations.AddField(
            model_name='cuota',
            name='week',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='mainapp.Week'),
        ),
    ]

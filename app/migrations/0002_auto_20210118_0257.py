# Generated by Django 2.2.17 on 2021-01-18 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='Maestro_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Maestro'),
        ),
    ]

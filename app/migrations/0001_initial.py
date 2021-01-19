# Generated by Django 2.2.17 on 2021-01-18 09:27

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
            name='Alumno',
            fields=[
                ('Matricula_ID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Paterno', models.CharField(max_length=100)),
                ('Materno', models.CharField(max_length=100)),
                ('Nombre', models.CharField(max_length=100)),
                ('Grupo', models.CharField(max_length=4)),
                ('Inscrito', models.BooleanField()),
            ],
            options={
                'db_table': 'alumno',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('Materia_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Encab', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'materia',
            },
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('Filiacion', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Paterno', models.CharField(max_length=100)),
                ('Materno', models.CharField(max_length=100)),
                ('Nombre', models.CharField(max_length=100)),
                ('CURP', models.CharField(max_length=17)),
                ('Numero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'maestro',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo_ID', models.CharField(default='2020-2021', max_length=10)),
                ('Semestre', models.CharField(max_length=3)),
                ('Calif_Parcial_1', models.CharField(max_length=3)),
                ('Calif_Parcial_2', models.CharField(max_length=3)),
                ('Calif_Parcial_3', models.CharField(max_length=3)),
                ('Materia_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Materia')),
                ('Matricula_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Alumno')),
            ],
            options={
                'db_table': 'historial',
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('Grupo_ID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Maestro_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Maestro')),
                ('Materia_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Materia')),
            ],
            options={
                'db_table': 'clase',
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='Maestro_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Materia'),
        ),
    ]
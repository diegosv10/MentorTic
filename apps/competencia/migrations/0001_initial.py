# Generated by Django 2.0.7 on 2019-04-11 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entidad', '0001_initial'),
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre competencia')),
                ('duracion', models.CharField(max_length=10, verbose_name='Duracion competencia')),
            ],
            options={
                'verbose_name': 'Competencia',
                'verbose_name_plural': 'Competencias',
            },
        ),
        migrations.CreateModel(
            name='CompLograda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=30, verbose_name='Grado')),
                ('especialidad', models.CharField(max_length=30, verbose_name='Especialidad')),
                ('puesto', models.CharField(max_length=30, verbose_name='Puesto')),
                ('periodo', models.CharField(max_length=30, verbose_name='Periodo')),
                ('DNI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CompLograda', to='mentor.Mentor')),
                ('IDComp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CompLograda', to='competencia.Competencia')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CompLograda', to='entidad.Entidad')),
            ],
            options={
                'verbose_name': 'Competencia lograda',
                'verbose_name_plural': 'Competencias logradas',
            },
        ),
        migrations.CreateModel(
            name='CompPlanif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=30, verbose_name='Periodo')),
                ('estado', models.CharField(max_length=30, verbose_name='Estado')),
                ('IDComp', models.ForeignKey(on_delete=True, related_name='CompPlanif', to='competencia.Competencia')),
                ('IDSes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CompPlanif', to='mentor.Mentoria')),
            ],
            options={
                'verbose_name': 'Competencia planificada',
                'verbose_name_plural': 'Competencias planificadas',
            },
        ),
        migrations.CreateModel(
            name='Referente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.FloatField(verbose_name='Puntaje')),
                ('DNI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Referente', to='mentor.Mentor')),
                ('IDComp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Referente', to='competencia.Competencia')),
            ],
            options={
                'verbose_name': 'Referente',
                'verbose_name_plural': 'Referentes',
            },
        ),
    ]

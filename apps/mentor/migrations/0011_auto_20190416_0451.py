# Generated by Django 2.0.7 on 2019-04-16 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0010_auto_20190413_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='DNIUpline',
        ),
        migrations.AlterField(
            model_name='mentor',
            name='DNI',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='tipo',
            field=models.CharField(blank=True, choices=[('APRENDIZ', 'Aprendiz'), ('MENTOR', 'Mentor')], default='Aprendiz', max_length=10, null=True, verbose_name='Tipo'),
        ),
    ]

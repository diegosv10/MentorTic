# Generated by Django 2.0.7 on 2019-04-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0016_auto_20190425_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Aprendiz', 'Aprendiz'), ('Mentor', 'Mentor')], default='Aprendiz', max_length=10, null=True, verbose_name='Tipo'),
        ),
    ]

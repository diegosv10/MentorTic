# Generated by Django 2.0.7 on 2019-04-25 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competencia', '0005_auto_20190425_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoja_vida',
            name='entidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hojaVida', to='entidad.Entidad'),
        ),
    ]

# Generated by Django 2.0.7 on 2019-05-03 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0018_remove_mentor_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mentor', to='ubigeos.Distrito'),
        ),
    ]
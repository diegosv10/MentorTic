# Generated by Django 2.0.7 on 2019-04-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0011_auto_20190416_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='wannaBeMentor',
            field=models.BooleanField(default=False, verbose_name='Quiero ser mentor'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachaqtec', '0002_auto_20201211_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='cursos',
            field=models.ManyToManyField(db_table='matricula', to='pachaqtec.Cursos'),
        ),
    ]
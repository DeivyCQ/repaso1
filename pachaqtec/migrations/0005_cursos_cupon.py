# Generated by Django 3.1.4 on 2020-12-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachaqtec', '0004_categoria_cupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='cupon',
            field=models.ManyToManyField(to='pachaqtec.Cupon'),
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachaqtec', '0003_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='cupon',
            field=models.ManyToManyField(to='pachaqtec.Cupon'),
        ),
    ]

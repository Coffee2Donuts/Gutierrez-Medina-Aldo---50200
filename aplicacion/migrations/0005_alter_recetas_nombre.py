# Generated by Django 5.0.1 on 2024-02-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_remove_recetas_n_recetas_remove_recetas_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
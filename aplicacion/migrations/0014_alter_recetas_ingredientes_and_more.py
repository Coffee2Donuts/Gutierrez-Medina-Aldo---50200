# Generated by Django 5.0.1 on 2024-03-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0013_rename_autor_comentario_usuario_comentario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='ingredientes',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='procedimiento',
            field=models.CharField(max_length=1500),
        ),
    ]

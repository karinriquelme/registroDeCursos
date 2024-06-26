# Generated by Django 4.2 on 2024-05-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_direccion_estudiante_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='estudiante_id',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='profesor_id',
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiante_id',
            field=models.ManyToManyField(to='app.estudiante'),
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor_id',
            field=models.ManyToManyField(to='app.profesor'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('accion', models.TextField(verbose_name='Accion')),
                ('usuario', models.CharField(max_length=50, verbose_name='usuario')),
            ],
        ),
    ]

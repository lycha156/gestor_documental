# Generated by Django 3.1.2 on 2022-10-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependencias', '0002_alter_dependencia_direccion_alter_dependencia_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencia',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tipodependencia',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
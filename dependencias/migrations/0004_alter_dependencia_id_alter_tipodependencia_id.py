# Generated by Django 4.0.4 on 2022-10-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependencias', '0003_auto_20221027_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tipodependencia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='codigo',
            field=models.CharField(max_length=50, verbose_name='Codigo'),
        ),
    ]

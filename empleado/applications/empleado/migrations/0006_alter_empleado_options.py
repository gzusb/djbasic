# Generated by Django 4.1.1 on 2022-09-16 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['id'], 'verbose_name': 'Mis Empleados', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
    ]

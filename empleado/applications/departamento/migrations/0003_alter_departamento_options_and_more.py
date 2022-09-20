# Generated by Django 4.1.1 on 2022-09-12 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_short_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
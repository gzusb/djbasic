from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades de los empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):

    JOBS = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_name = models.CharField('Full Name', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOBS)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades, blank=True)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mis Empleados'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['id']


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name 
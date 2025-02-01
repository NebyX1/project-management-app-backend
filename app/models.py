from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Project(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID del Proyecto")
    description = models.TextField(verbose_name="Descripción")
    name = models.CharField(max_length=255, verbose_name="Nombre del Proyecto")
    office = models.CharField(max_length=255, verbose_name="Oficina")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación"
    )
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="Última Actualización"
    )
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID de la Tarea")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks", verbose_name="Proyecto"
    )
    name = models.CharField(max_length=255, verbose_name="Nombre de la Tarea")
    description = models.TextField(verbose_name="Descripción")
    responsible = models.CharField(max_length=255, verbose_name="Responsable")
    start_date = models.DateField(verbose_name="Fecha de Inicio")
    due_date = models.DateField(verbose_name="Fecha de Vencimiento")
    priority = models.CharField(
        max_length=50,
        choices=[("Alta", "Alta"), ("Media", "Media"), ("Baja", "Baja")],
        verbose_name="Prioridad",
    )
    status = models.CharField(
        max_length=50,
        choices=[
            ("Por Hacer", "Por Hacer"),
            ("En Progreso", "En Progreso"),
            ("En Revisión", "En Revisión"),
            ("Terminado", "Terminado"),
        ],
        verbose_name="Estado",
    )

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.name

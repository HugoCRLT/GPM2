from django.conf import settings
from django.db import models
from django.utils import timezone


class Equipe(models.Model):
    equipe = models.CharField(verbose_name='Equipe', max_length=250, unique=True)
    encarregado = models.CharField(verbose_name='Encarregado', max_length=100)
    supervisor = models.CharField(verbose_name='Supervisor', max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now, blank=True, null=True, editable=False)
    data_modificacao = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.equipe
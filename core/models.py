from django.db import models


class Base(models.Model):
    criado = models.DateTimeField('Criado em', auto_now_add=True, auto_now=False)
    modificado = models.DateTimeField('Modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
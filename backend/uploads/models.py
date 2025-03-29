'''from django.db import models

class Arquivo(models.Model):
    nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='arquivos/')

    def __str__(self):
        return self.nome
'''
from django.db import models

class Arquivo(models.Model):
    # Remova esse campo se ele for obrigatório:
    # nome = models.CharField(max_length=100)
    # Ou altere para opcional:
    nome = models.CharField(max_length=100, blank=True, null=True)

    arquivo = models.FileField(upload_to='uploads/')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arquivo.name

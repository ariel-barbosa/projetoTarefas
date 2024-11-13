from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=255),
    email = models.EmailField(max_length=255)
    class Meta:
        db_table = 'tbl_usuarios'

class Tarefas(models.Model):
    descricao = models.CharField(255),
    setor = models.CharField(255),
    proridade   = models.CharField(255),
    status = models.CharField(255),
    data = models.DateField
    class Meta:
        db_table = 'tbl_tarefas'


    
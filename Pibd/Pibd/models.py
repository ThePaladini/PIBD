from django.db import models

class ComponenteCurricular(models.Model):
    nome_componente = models.CharField(max_length=100)
    nome_idioma = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    carga_teorica = models.IntegerField()
    eixo_tematico = models.CharField(max_length=50)
    obrigatoriedade = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'componente_curricular'

from django.db import models
from uploader.models import Image
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculo")
    descricao = models.CharField(max_length=2500, null=True, blank=True)
    foto = models.ManyToManyField(Image, related_name="+", blank=True)
    
    def __str__(self):
        return f"{self.modelo} {self.ano}" 
    
    class Meta:
        verbose_name = "Veículo"

    class Meta:
        verbose_name_plural = "Veículos"
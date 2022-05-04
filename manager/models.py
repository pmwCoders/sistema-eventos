from django.db import models
from users.models import User


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    palestrante = models.CharField(max_length=50)
    inicio = models.TimeField(auto_now=False, auto_now_add=False)
    fim = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome

class Presenca(models.Model):
    espectador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    data = models.DateField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        presenca = str(self.espectador)+" | "+str(self.evento)+" | "+str(self.data)
        return presenca
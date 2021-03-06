from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

#CUSTOM USER MODEL
class User(AbstractUser):
    username = models.EmailField(_('username'), unique=False)
    email = models.EmailField(_('email address'), unique=True)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        nome = self.username
        return nome

#USER PROFILES
class EstudanteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='estudante_profile')
    matricula = models.CharField(max_length=50)
    curso = models.CharField(max_length=100)

    def __str__(self):
        nome = self.user.first_name+" "+self.user.last_name
        return nome

class VisitanteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='visitante_profile')
    campoextra = models.CharField(max_length=100, null=True)

    def __str__(self):
        nome = self.user.first_name+" "+self.user.last_name
        return nome

#SIGNAL METHODS TO ASSOCIATE THE USER MODEL WITH THE USER PROFILES
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.tipo == "Estudante":
		EstudanteProfile.objects.get_or_create(user = instance)
	elif instance.tipo == "Visitante":
		VisitanteProfile.objects.get_or_create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	if instance.tipo == "Estudante":
		instance.estudante_profile.save()
	elif instance.tipo == "Visitante":
		instance.visitante_profile.save()
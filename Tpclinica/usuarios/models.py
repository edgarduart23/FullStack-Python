from django.db import models
from django.contrib.auth.models import AbstractUser
# from __future__ import unicode_literals

# Create your models here.
class User(AbstractUser):
    es_secretaria = models.BooleanField(default=False)
    es_medico = models.BooleanField(default=False)
    es_taller = models.BooleanField(default=False)
    es_ventas = models.BooleanField(default=False)
    es_gerencia = models.BooleanField(default=False)
# 
    # def get_perfil_secretaria(self):
        # perfil_secretaria = None
        # if hasattr(self, 'perfilsecretaria'):
            # perfil_secretaria = self.perfilsecretaria
        # return perfil_secretaria
    # 
    # def get_perfil_medico(self):
        # perfil_medico = None
        # if hasattr(self, 'perfilmedico'):
            # perfil_medico = self.perfilmedico
        # return perfil_medico
    # 
    # def get_perfil_taller(self):
        # perfil_taller = None
        # if hasattr(self, 'perfiltaller'):
            # perfil_taller = self.perfiltaller
        # return perfil_taller
    # 
    # def get_perfil_ventas(self):
        # perfil_ventas = None
        # if hasattr(self, 'perfilventas'):
            # perfil_ventas = self.perfilventas
        # return perfil_ventas
    # 
    # def get_perfil_gerencia(self):
        # perfil_gerencia = None
        # if hasattr(self, 'perfilgerencia'):
            # perfil_gerencia = self.perfilgerencia
        # return perfil_gerencia

    class Meta:
        db_table = 'auth_user'
# 
# class PerfilSecretaria(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)
    # name = models.CharField(max_length=64)
# 
# class PerfilMedico(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)
    # name = models.CharField(max_length=64)
# 
# class PerfilTaller(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)
    # name = models.CharField(max_length=64)
# 
# class PerfilVentas(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)
    # name = models.CharField(max_length=64)
# 
# class PerfilGerencia(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)
    # name = models.CharField(max_length=64)
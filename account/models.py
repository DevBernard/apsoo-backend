from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    def _create_user(self, email, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Insira um E-mail, caralho')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        return self._create_user(email,password)

    def create_staffuser(self, email, password=None):
        return self._create_user(email, password, is_staff=True)

    def create_superuser(self, email, password=None):
        return self._create_user(email, password, is_staff=True, is_admin=True)
        

class Usuario(AbstractBaseUser):
    email = models.EmailField("E-mail", unique=True)
    date_joined = models.DateTimeField("Criado em", default=timezone.now)

    is_active = models.BooleanField('Ativo', default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_admin = models.BooleanField('Administrador', default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True 
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        MANAGER = 'manager', _('Manager')
        DEPARTMENT_MANAGER = 'department_manager', _('Department Manager')
        USER = 'user', _('User')

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name=_('Role'),
    )
    department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name=_('Department'),
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Department Name'))

    def __str__(self):
        return self.name
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    CHOICES = [(USER, 'user'), (ADMIN, 'admin')]


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    role = models.CharField(choices=UserRoles.CHOICES, default=UserRoles.USER, max_length=50)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def objects(self):
        from .managers import UserManager
        return UserManager()

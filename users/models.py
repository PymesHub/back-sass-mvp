from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=5, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custm_user_permissons",
        blank=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "STUDENT", 'Student'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.STAFF)


class Student(User):
    base_role = User.Role.STUDENT

    staff = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only For Student"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
            return super().save(*args, **kwargs)    

from django.db import models
from django.contrib.auth.models import AbstractUser
from.validators import phone_validator


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, validators=[phone_validator])
    
    def __str__(self):
        return f'{self.first_name}'
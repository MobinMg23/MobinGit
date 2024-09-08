from django.db import models
from users.models import User


class Car(models.Model):
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    year_of_production = models.PositiveIntegerField()
    km = models.PositiveBigIntegerField()
    descriptions = models.TextField(max_length=300, blank=True, null=True)
    price = models.CharField(max_length=20)
    car_from = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f'{self.model}'
    

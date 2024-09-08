from django.contrib import admin
from .models import Car
from users.models import User
# Register your models here.
admin.site.register(Car)
admin.site.register(User)


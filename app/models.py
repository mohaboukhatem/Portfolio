from pydoc import describe
from django.db import models


class contact (models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = 
    description = 
    created = 
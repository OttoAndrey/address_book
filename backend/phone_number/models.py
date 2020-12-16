from django.db import models

from users.models import Users


class PhoneNumber(models.Model):
    MOBILE = 'M'
    CITY = 'C'
    TYPES = [
        (MOBILE, 'Mobile'),
        (CITY, 'City')
    ]

    number = models.CharField(max_length=11)
    type = models.CharField(max_length=2, choices=TYPES)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

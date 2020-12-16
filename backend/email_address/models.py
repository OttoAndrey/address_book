from django.db import models

from users.models import Users


class EmailAddress(models.Model):
    PERSONAL = 'P'
    WORK = 'W'
    TYPES = [
        (PERSONAL, 'Personal'),
        (WORK, 'Work')
    ]

    email = models.EmailField()
    type = models.CharField(max_length=2, choices=TYPES)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

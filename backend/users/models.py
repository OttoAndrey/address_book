from django.db import models


class Users(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    GENDERS = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other')
    ]

    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, upload_to='avatars')
    gender = models.CharField(max_length=2, choices=GENDERS)
    birth_date = models.DateField()
    living_address = models.TextField()

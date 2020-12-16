from django.db import migrations
from faker import Faker
import random


def fill_db(apps, schema):
    fake = Faker('ru_RU')
    Users = apps.get_model('users', 'Users')
    EmailAddress = apps.get_model('email_address', 'EmailAddress')
    PhoneNumber = apps.get_model('phone_number', 'PhoneNumber')

    users = []
    phone_numbers = []
    email_addresses = []

    for i in range(100):
        profile = fake.profile()
        user = Users(full_name=profile['name'],
                     gender=profile['sex'],
                     birth_date=profile['birthdate'],
                     living_address=profile['address'])
        users.append(user)

    Users.objects.bulk_create(users)

    for user in Users.objects.all():
        fake_phone_number = fake.phone_number()
        clean_number = ''.join(number for number in fake_phone_number if number.isdigit())
        phone_type = random.choice(['M', 'C'])
        phone_number = PhoneNumber(number=clean_number,
                                   type=phone_type,
                                   user=user)
        phone_numbers.append(phone_number)

        email = fake.email()
        email_type = random.choice(['P', 'W'])
        email_address = EmailAddress(email=email,
                                     type=email_type,
                                     user=user)
        email_addresses.append(email_address)

    PhoneNumber.objects.bulk_create(phone_numbers)
    EmailAddress.objects.bulk_create(email_addresses)


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_db)
    ]

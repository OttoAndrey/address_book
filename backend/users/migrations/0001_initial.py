# Generated by Django 3.1.4 on 2020-12-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(null=True, upload_to='avatars')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=2)),
                ('birth_date', models.DateField()),
                ('living_address', models.TextField()),
            ],
        ),
    ]

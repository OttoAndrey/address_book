from rest_framework import serializers

from users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['full_name', 'avatar', 'gender', 'birth_date', 'living_address']

from rest_framework import serializers

from email_address.models import EmailAddress


class EmailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = ['email', 'type', 'user']

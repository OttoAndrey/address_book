from rest_framework import viewsets, filters

from email_address.models import EmailAddress
from email_address.serializers import EmailAddressSerializer


class EmailAddressViewSet(viewsets.ModelViewSet):
    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['email', 'type', 'user']

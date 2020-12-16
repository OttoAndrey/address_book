from rest_framework import viewsets, filters

from phone_number.models import PhoneNumber
from phone_number.serializers import PhoneNumberSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['number', 'type', 'user']

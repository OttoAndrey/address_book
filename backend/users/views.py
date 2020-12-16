from rest_framework import viewsets, filters

from users.models import Users
from users.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['full_name', 'avatar', 'gender', 'birth_date', 'living_address']

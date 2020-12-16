from rest_framework import routers

from email_address.views import EmailAddressViewSet
from phone_number.views import PhoneNumberViewSet
from users.views import UsersViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('phonenumber', PhoneNumberViewSet, basename='phonenumber')
router.register('emailaddress', EmailAddressViewSet, basename='emailaddress')

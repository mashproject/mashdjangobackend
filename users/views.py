from rest_framework import filters
from rest_framework.generics import ListAPIView
from users.models import CustomUser
from users.serializer import UserDetailedSerializer


class RetrieveAll(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailedSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('department', 'id')

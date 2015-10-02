from rest_framework import filters
from events.serializer import EventSerializer
from rest_framework.generics import ListAPIView

from events.models import Events


class RetrieveAll(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('is_published', 'type_id', 'id')

# class RetrieveByIdView(RetrieveAPIView):
#     queryset = Events.objects.all()
#     serializer_class = EventSerializer

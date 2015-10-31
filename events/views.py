import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters
from events.serializer import EventSerializer
from rest_framework.generics import ListAPIView
from events.models import Event, Supporter


class RetrieveAll(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('is_published', 'type_id', 'id',)


@api_view(['POST'])
def get_all_suppporters(request):
    logging.info(dir(request))
    ids = request.data.get('ids', [])
    if ids:
        supports = Supporter.objects.filter(pk__in=ids).values()
        return Response(supports)
    return Response('No data found')

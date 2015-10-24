from rest_framework.filters import FilterSet
from events.models import Events, Supporters
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'image_url',
                  'is_published', 'pub_date', 'gallery_div',
                  'type_id','supporters')



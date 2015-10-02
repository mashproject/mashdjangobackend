from django.db import models

class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    id = models.IntegerField(unique=True, primary_key=True)


TYPES = ((event_type.id, event_type.name) for event_type in EventType.objects.all())


class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    edit_date = models.DateField('date edited', auto_now=True)
    pub_date = models.DateField('date published', auto_now=False, null=True)
    is_published = models.BooleanField(default=False)
    type_id = models.IntegerField(default=0, choices=TYPES)
    gallery_div = models.TextField()

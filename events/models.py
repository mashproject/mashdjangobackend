from django.db import models

TYPES = (
    (0, 'Default'),
    (1, 'Events'),
)


class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    edit_date = models.DateField('date edited', auto_now=True)
    pub_date = models.DateField('date published', auto_now=False, null=True)
    is_published = models.BooleanField(default=False)
    type_id = models.IntegerField(default=0, choices=TYPES)
    gallery_div = models.TextField()

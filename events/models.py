from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    edit_date = models.DateField('date edited', auto_now=True)
    pub_date = models.DateField('date published', auto_now=False, null=True)
    is_published = models.BooleanField(default=False)
    type_id = models.IntegerField(default=0, choices=[(0, b'Default'), (1, b'Events')])
    gallery_div = models.TextField()

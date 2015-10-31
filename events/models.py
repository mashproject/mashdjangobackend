import os

from django.db import models


def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT,/user_<id>/<filename>
    ext = '.' + filename.split('.')[-1]
    image_id = ''.join((instance.title.replace(' ', '_'), str(instance.type_id)))
    return os.path.join(str(instance.__class__.__name__), str(image_id + ext))


EVENT_TYPE = ((0, 'Default'), (1, 'Mixers'), (2, 'Workshops'), (
    3, 'Open Dialogues'), (4, 'Mash ups'), (5, 'Culture'))

SUPPORTERS_TYPE = ((0, 'Organiser'), (1, 'Sponsors'))


class Supporter(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.ImageField(upload_to=image_path, blank=True)
    type_id = models.IntegerField(default=0, choices=SUPPORTERS_TYPE)
    url = models.URLField(null=True,blank=True)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.ImageField(upload_to=image_path, blank=True)
    edit_date = models.DateField('date edited', auto_now=True)
    pub_date = models.DateField('date published', auto_now=False, null=True,blank=True)
    is_published = models.BooleanField(default=False)
    type_id = models.IntegerField(default=0, choices=EVENT_TYPE)
    gallery_div = models.TextField(blank=True)
    location = models.CharField(max_length=50, null=True,blank=True)
    regiteration_link = models.URLField(null=True,blank=True)
    url = models.URLField(null=True, blank=True)
    supporters = models.ManyToManyField(Supporter,blank=True)

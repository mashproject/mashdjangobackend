from django.contrib import admin

# Register your models here.
from events.models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'edit_date', 'is_published')




admin.site.register(Events, EventsAdmin)


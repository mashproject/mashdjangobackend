from django.contrib import admin

# Register your models here.
from events.models import Events, EventType


class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'edit_date', 'is_published')


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Events, EventsAdmin)
admin.site.register(EventType, EventTypeAdmin)

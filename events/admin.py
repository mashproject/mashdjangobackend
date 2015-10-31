from django.contrib import admin

# Register your models here.
from events.models import Event, Supporter


class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'edit_date', 'is_published')
    filter_horizontal = ('supporters',)


class SupportersAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'type_id')


admin.site.register(Supporter, SupportersAdmin)
admin.site.register(Event, EventsAdmin)

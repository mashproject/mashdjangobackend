from django.contrib import admin

# Register your models here.
from events.models import Events, Supporters


class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'edit_date', 'is_published')
    filter_horizontal = ('supporters',)


class SupportersAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'type_id')


admin.site.register(Supporters, SupportersAdmin)
admin.site.register(Events, EventsAdmin)

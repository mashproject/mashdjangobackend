from django.shortcuts import get_object_or_404
from multiupload.admin import MultiUploadAdmin
from django.contrib import admin

# Register your models here.
from events.models import Event, Supporter, Image

class ImageInlineAdmin(admin.TabularInline):
    model = Image

class EventsAdmin(MultiUploadAdmin):
    list_display = ('title', 'edit_date', 'is_published')
    filter_horizontal = ('supporters',)
    inlines = [ImageInlineAdmin,]
    multiupload_form = True
    multiupload_list = False
    # change_form_template = 'events/change_form.html'
    # multiupload_template = 'events/upload.html'


    def process_uploaded_file(self, uploaded, object, request):
        if object:
            image = object.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, gallery=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()


class SupportersAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'type_id')


admin.site.register(Supporter, SupportersAdmin)
admin.site.register(Event, EventsAdmin)

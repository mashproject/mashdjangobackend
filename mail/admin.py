from django.conf.urls import url
from django.contrib import admin

# Register your models here.
from django.core.urlresolvers import reverse
from mail import views
from mail.models import Mail


class SendMailAdmin(admin.ModelAdmin):
    list_display = ('email',)
    change_list_template = 'mail/change_list.html'

    def get_urls(self):
        urls = super(SendMailAdmin, self).get_urls()
        external_urls = [
            url(r'^send_mail/$', views.SendMail().as_view(), name='send_mail'),
        ]
        return external_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'send_mail_url': reverse('admin:%s' % 'send_mail'),
        })
        return super(SendMailAdmin, self).changelist_view(request, extra_context)


admin.site.register(Mail, SendMailAdmin)

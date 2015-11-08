from django.contrib.auth.admin import UserAdmin
from users.models import User

from django.contrib import admin
from django.utils.translation import ugettext as _


# class AdminImageWidget(AdminFileWidget):
#     def render(self, name, value, attrs=None):
#         output = []
#         if value and getattr(value, "url", None):
#             image_url = value.url
#             file_name=str(value)
#             output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % \
#                 (image_url, image_url, file_name, _('Change:')))
#         output.append(super(AdminFileWidget, self).render(name, value, attrs))
#         return mark_safe(u''.join(output))

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'),
         {'fields': (
         'first_name', 'last_name', 'department', 'profile_pic', 'fb_profile', 'about_user', 'linkedin_profile',
         'twitter_profile','about_me_profile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('date_joined', 'last_login')
    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name == 'profile_pic':
    #         request = kwargs.pop("request", None)
    #         kwargs['widget'] = AdminImageWidget
    #         return db_field.formfield(**kwargs)
    #     return super(CustomUserAdmin,self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(User, CustomUserAdmin)

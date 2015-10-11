import os

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

DEPARTMENTS = ((0, 'Technical'), (1, 'Communication'), (2, 'Events'), (
    3, 'Human Resourse'), (4, 'Finance'), (5, 'Advisors'), (6, 'Admin'))


def user_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ext = '.' + filename.split('.')[-1]
    return os.path.join('users', str(instance.id) + ext)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True, )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    fb_profile = models.URLField()
    about_user = models.TextField()
    linkedin_profile = models.URLField()
    twitter_profile = models.URLField(blank=True)
    about_me_profile = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to=user_image_path, blank=True)
    department = models.IntegerField(choices=DEPARTMENTS, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def image_tag(self):
        return u'<img src="%s" />' % self.profile_pic

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

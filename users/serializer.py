from rest_framework import serializers
from users.models import CustomUser

__author__ = 'aman'


class UserDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'first_name', 'last_name', 'fb_profile',
                  'profile_pic', 'department','username','about_user',
                  'linkedin_profile','twitter_profile','about_me_profile')

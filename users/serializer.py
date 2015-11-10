from rest_framework import serializers

from users.models import User

__author__ = 'aman'


class UserDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'fb_profile',
                  'profile_pic', 'department', 'username', 'about_user',
                  'linkedin_profile', 'twitter_profile', 'about_me_profile', 'about_user')

from rest_framework import serializers
from articles.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = serializers.ALL_FIELDS

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = serializers.ALL_FIELDS

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """

        validated_data['user']['password'] = make_password(validated_data['user']['password'])
        validated_data['user']['is_active'] = True
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        userprofile, created = UserProfile.objects.update_or_create(user=user,
                                                                avatar=validated_data.pop('avatar'))
        return userprofile
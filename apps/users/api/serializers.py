from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    """ Serializes the user parameters """
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

    def to_representation(self, instance):
        # data = super().to_representation(instance)
        # print(data)
        # print(type(instance))
        return {
            'id':instance['id'],
            'username':instance['username'],
            'email':instance['email'],
            'password':instance['password']
        }
        
        # print(type(instance))
        # return {
        #     'id':instance.id,
        #     'username':instance.username,
        #     'email':instance.email,
        #     'password':instance.password
        # }
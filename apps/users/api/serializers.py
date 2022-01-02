from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    """ Serializes the user parameters """
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):
        # Custom validation
        if 'admin' in value:
            raise serializers.ValidationError('Error, a user with this name cannot exist')
        print(value)
        return value

    def validate_email(self, value):
        # Custom validation
        if 'test' not in value:
            raise serializers.ValidationError('Error, test must be in the e-mail')
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('Error, e-mail cannot contain the name')     
        print(value)
        return value

    def validate(self, data):
        #if data['name'] in data['email']:
        #    raise serializers.ValidationError('The email cannot contain the name')
        #print('General validate')
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
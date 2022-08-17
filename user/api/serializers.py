from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'userName', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# from rest_framework import serializers
# from ..models import Users

# class UsersSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = Users
#         fields = '__all__'

#     def create(self, validated_data):
#         user = super(UsersSerializer, self).create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
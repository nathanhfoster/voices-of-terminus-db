from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author_name')
    class Meta:
        model = User
        fields = (
        'id', 'username', 'password', 'first_name', 'last_name',
        'bio', 'profile_image', 'primary_role', 'secondary_class', 'secondary_role', 
        'last_login', 'is_superuser', 'email', 'is_staff',
        'is_active', 'date_joined',  
        'discord_url', 'twitter_url', 'twitch_url', 'youtube_url',
        'primary_class', )
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
   

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password'])
            )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    # def patch(self, request, pk):
    #     testmodel = self.get_object(pk)
    #     serializer = UserSerializer(testmodel, data=request.data, partial=True) # set partial=True to update a data partially
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonReponse(code=201, data=serializer.data)
    #     return JsonResponse(code=400, data="wrong parameters")
    
    # def restore_object(self, attrs, instance=None):
    #     # call set_password on user object. Without this
    #     # the password will be stored in plain text.
    #     user = super(UserSerializer, self).restore_object(attrs, instance)
    #     user.set_password(attrs['password'])
    #     return user

from rest_framework import serializers
from django.contrib.auth import get_user_model



User = get_user_model()
class UserModelSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True,write_only=True)
    password2 = serializers.CharField(required=True,write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',

        ]
        extra_kwargs ={
            'password1':{'write_only':True},
            'password2':{'write_only':True},
            }

    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password1 = validated_data.get('password1')
        password2 = validated_data.get('password2')
        if password1 == password2:
            user = User.objects.create(username = username,password = password1)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password1)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error':"Both Password is not same"
            })


        return super().create(validated_data)
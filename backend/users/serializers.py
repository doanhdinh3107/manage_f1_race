from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    #dinh nghia model
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        #dinh nghia model dc sẻializer su dung
        model = NewUser
        #cac truong ma serializer se tra ve
        fields = ('email', 'user_name', 'password')
        #password chi su dung de ghi k su dung de public data
        extra_kwargs = {'password': {'write_only': True}}
#lop tao doi tg tu seli
    def create(self,validated_data):
        #lay du lieu xong xoa luon du lieu thnah   none
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        #user dc khoi tao tu cac gia tri data
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
from rest_framework import serializers
from .models import Video, Rating, GpuStatus
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class GpuStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpuStatus
        fields = ('create_date', 'server_name', 'server_group', 'label_gpu', 'index_gpu', 'util_gpu')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video

        # 전부 다 가지고 오고 싶은 경우
        # fields ='__all__'
        fields = (
        'id', 'title', 'description', 'rating_average', 'url', 'category', 'subcategory', 'author', 'comments_list')

        # serializer할때 url 필수 등록해야함을 명시
        extra_kwargs = {'url': {'required': True}}


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'video', 'comments')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

        # serializer할때 데이터 베이스에서 불려올때 write만 되게 한다.
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        # 인증 추가
        Token.objects.create(user=user)
        return user

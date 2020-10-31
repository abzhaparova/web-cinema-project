from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User, Movie, Comment
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=False)
    comment_page_id = serializers.IntegerField(write_only=False)

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=False)

    class Meta:
        model = Comment
        fields = '__all__'


# class CommentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(write_only=True)
#     username = serializers.CharField()
#     message = serializers.CharField()
#     date_posted = serializers.DateTimeField(default=datetime.now())
#     comment_page = serializers.CharField()
#
#     def create(self, validated_data):
#         # comment = Comment.objects.create(username = validated_data.get('username'),
#         #                                  message = validated_data.get('message'),
#         #                                  date_posted = validated_data.get('date_posted'),
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.message = validated_data.get('message', instance.message)
#         instance.date_posted = validated_data.get('date_posted', instance.date_posted)
#         instance.comment_page = validated_data.get('comment_page', instance.comment_page)
#         instance.save()
#         return instance


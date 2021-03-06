from rest_framework import serializers

from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

# import tracks.models as Track
# from tracks.models import Track
# from artists.models import Artist
# from .models import Album

from django.apps import apps
from likes import services as likes_services

# Track = apps.get_model(app_label='tracks', model_name='Track')
Artist = apps.get_model(app_label='artists', model_name='Artist')
Album = apps.get_model(app_label='albums', model_name='Album')
# Like = apps.get_model(app_label='likes', model_name='Like')
Image = apps.get_model(app_label='images', model_name='Image')


class ArtistsSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'artist_uri',

        ]

    def get_id(self, obj):

        return obj.artist_uri


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = [
            # 'id',
            'url',
            'height',
            'width',

        ]


class AlbumsSerializer(serializers.ModelSerializer):
    artists = ArtistsSerializer(many=True)
    # tracks = serializers.SerializerMethodField()
    images = ImagesSerializer(many=True)
    is_liked = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    # posts = PostsSerializer(many=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            # 'tracks',
            'artists',
            # 'images',
            # 'album_id',
            'album_uri',
            'images',
            'is_liked',
            # 'likes_count',
            'total_likes',
            # 'created_at',
            # 'updated_at',
            # 'likes_count',
        ]

    def get_id(self, obj):

        return obj.album_uri

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        # user = self.context['request'].user
        return likes_services.is_fan(obj, user)

    def get_total_likes(self, obj):
        return likes_services.get_object_likes_count(obj)


class ArtistSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255, min_length=3, read_only=True)
    # album_id = serializers.CharField()
    # artists = ArtistsSerializer
    # tracks = TrackSerializer(many=True)
    images = ImagesSerializer(many=True)
    # tracks = TrackSerializer()
    # posts = PostsSerializer()
    albums = AlbumsSerializer(many=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = [
            'id',
            # 'uuid',
            'name',
            'artist_uri',
            'images',
            # 'album_id',

            'albums',
            # 'images',
            # 'created_at',
            # 'updated_at',
            # 'likes_count',
        ]

    def get_id(self, obj):

        return obj.artist_uri

class ArtistListSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255, min_length=3, read_only=True)
    # album_id = serializers.CharField()
    # artists = ArtistsSerializer
    # tracks = TrackSerializer(many=True)
    # tracks = TrackSerializer()
    # posts = PostsSerializer()
    images = ImagesSerializer(many=True)
    # albums = AlbumsSerializer(many=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = [
            'id',
            # 'uuid',
            'name',
            'artist_uri',
            # 'album_id',
            # 'artists',
            # 'albums',
            'images',
            # 'created_at',
            # 'updated_at',
            # 'likes_count',
        ]

    def get_id(self, obj):

        return obj.artist_uri

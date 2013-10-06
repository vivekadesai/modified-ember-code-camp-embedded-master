from rest_framework import serializers
from codecamp.ember.models import Session, Speaker, Rating, Tag, Location

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'description')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
	fields=('id','name')

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
	fields = ('id', 'name', 'session',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'score', 'feedback', 'session')

class SessionSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    speakers = SpeakerSerializer()
    ratings = RatingSerializer()
    tags = TagSerializer()

    class Meta:
        model = Session
        fields = ('id', 'name', 'room', 'desc', 'speakers', 'ratings', 'tags','location')

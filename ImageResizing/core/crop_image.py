from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    height = serializers.IntegerField()
    width = serializers.IntegerField()


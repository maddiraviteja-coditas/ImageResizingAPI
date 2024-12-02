# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .ImageSerializer import ImageSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .image_utils import crop_image
from .models import Image
from .crop_image import ImageSerializer
# Create your views here.


class HomeView(APIView):
    def __init__(self):
        pass

    def post(self, request):
        return Response("Hello")


class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Save the image
            instance = serializer.save()
            return Response(
                {
                    'status': 'success',
                    'data': {
                        'id': instance.id,
                    },
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageResizingView(APIView):
    def __init__(self):
        pass

    serializer_class = ImageSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_id = serializer.id;
            image = Image.objects.get(id=image_id)
            crop_image(image.image, serializer.data['x'], serializer.data['y'], serializer.data['width'], serializer.data['height'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
# EDA Packages
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils import image_convert
import cv2
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.
import easyocr
class ImageView(viewsets.ViewSet):
    def convertImage(self,request):
        reader = easyocr.Reader(['en'])
        data = request.data
        multiple_files = request.FILES
        img = multiple_files.getlist("media_file")[0]
        print(type(img))
        for i in range(len(multiple_files.getlist("media_file"))):

            print(multiple_files.getlist("media_file")[i])

            path = default_storage.save('a.png', ContentFile(img.read()))
        # cv2.imwrite("img", img)
            image_convert('a.png',reader=reader)
        return Response(
                    data={'status': True}, 
                    status=status.HTTP_200_OK
                )
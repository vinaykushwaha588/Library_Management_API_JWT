from lib2to3.pgen2 import token
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from account.serializers import UserModelSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class RegisterApiView(APIView):
    serializer_class = UserModelSerializer
    def post(self,reqeust, formate=None):
        serializer = self.serializer_class(data=reqeust.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_date = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user':serializer.data
            }
            return Response(response_date,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LogOutApiView(APIView):
    def post(self,request ,formant = None):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:        
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
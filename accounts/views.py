from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import *

# Create your views here.

class Register(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        student = request.query_params['student']
        dob = request.data['dob']
        if len(User.objects.filter(username=username))!=0:
            return Response({'success': False, "message": "Username already exists!!"},status=status.HTTP_400_BAD_REQUEST)
        user_object = User()
        user_object.username=username
        user_object.set_password(password)
        user_object.first_name=first_name
        user_object.last_name=last_name
        user_object.student=student
        user_object.dob=dob
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_object.save()        
        user = User.objects.get(username=username)
        if user.student:
            Student.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({"success": True, "message": "Your account has been successfully activated!!",
                'payload': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)},
                status=status.HTTP_202_ACCEPTED)

class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            serializer = RegisterSerializer(user)
            return Response({"success": True, "message": "Login successful",
                            'payload': serializer.data,
                            'refresh': str(refresh),
                            'access': str(refresh.access_token)},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'message':'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)
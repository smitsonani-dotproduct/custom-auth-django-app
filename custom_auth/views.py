from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import status
from custom_auth.serializers import RegisterSerializer, LoginSerializer
from django.http import JsonResponse

class RegisterView(APIView):
    # permission_classes = [AllowAny]

    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        print('serializers data =>',serializers.initial_data, type(serializers.initial_data)) # dict form of data 

        if serializers.is_valid():
            user = serializers.save()
            print('user =>', user)
            token, _ = Token.objects.get_or_create(user=user)
            print("Token =>",token)

            return Response(
                {
                    "token":token.key,
                },
                status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    # permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            print("Token =>",token)

            return Response({
                "token": token.key,
                "email": user.email
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DRF function-based view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TestFunctionAuthView(request):
    return JsonResponse({
        "message": "You are authenticated",
        "user": request.user.username or request.user.email
    })


# Use a DRF APIView (class-based)
class TestClassAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "You are authenticated",
            "user": request.user.username or request.user.email
        })
    
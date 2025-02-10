from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


@api_view(['POST'])

def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')
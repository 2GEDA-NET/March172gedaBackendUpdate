from ctypes import pointer
import json  # Add this import for JSON formatting
from datetime import timezone
from django.db.models import *
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.authentication import *
from .serializers import *
from django.middleware import csrf
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from user.authentication_backends import EmailOrPhoneNumberBackend
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth import authenticate, login
from rest_framework.views import *
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import status, permissions
from rest_framework import generics, filters, viewsets
from rest_framework.generics import *

# Create your views here.

# Authentication APIs
@api_view(['POST'])
@permission_classes([AllowAny])
def get_auth_token(request):
    # Retrieve the user from the request or any other authentication mechanism
    user = request.user

    # Create a token for the user (e.g., during registration or login)
    token, _ = Token.objects.get_or_create(user=user)

    # Retrieve the token value
    token_value = token.key

    return Response({'token': token_value})


def get_csrf_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'csrfToken': token})


@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        data = request.data
        email = data.get('email')
        phone_number = data.get('phone_number')


        # Debugging statement: Print the email and phone number
        print(f"Email: {email}, Phone Number: {phone_number}")

        if not email and not phone_number:
            return Response({'error': 'Either email or phone number must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserRegistrationSerializer(data=data, context={'request': request})

        if email:
            # Check if a user with the provided email already exists
            if User.objects.filter(email=email).exists():
                return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        elif phone_number:
            # Check if a user with the provided phone number already exists
            if User.objects.filter(phone_number=phone_number).exists():
                return Response({'error': 'User with this phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            try:
                user = serializer.save()
                token, created = Token.objects.get_or_create(user=user)
                token_key = token.key
                response_data = serializer.data
                response_data['token'] = token_key
                return Response(response_data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                print(e)  # Add this line to print the IntegrityError message
                return Response({'error': 'Account details already exist.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user

    if request.method == 'PUT':
        serializer = UserProfileUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User profile updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# End of Authentication APIs


# User List APIs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.all().order_by('date_joined')  # Retrieve users sorted by date of creation

    user_data = []
    for user in users:
        user_profile = UserProfile.objects.filter(user=user).first()  # Get the user's profile

        if user_profile:
            sticker_count = user_profile.stickers.count()
            sticking_count = UserProfile.objects.filter(stickers=user_profile).count()
        else:
            sticker_count = 0
            sticking_count = 0

        user_data.append({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'sticking_count': sticking_count,
            'sticker_count': sticker_count,
        })

    return Response(user_data, status=status.HTTP_200_OK)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        location_data = request.data.get('location')
        if location_data:
            # Assuming location_data is a dictionary with 'latitude' and 'longitude' keys
            latitude = location_data.get('latitude')
            longitude = location_data.get('longitude')

            # Create or update user location
            user = self.perform_create(serializer)
            user.location = pointer(longitude, latitude)  # Create a Point object from coordinates
            user.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# End of User details APIs


# Sticking APIs
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def stick_user(request, user_id):
    user = request.user.userprofile
    try:
        target_user = UserProfile.objects.get(pk=user_id)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if user != target_user:
        if user.sticking.filter(pk=user_id).exists():
            user.sticking.remove(target_user)
            return Response({"message": f"You unsticked {target_user.user.username}"})
        else:
            user.sticking.add(target_user)
            return Response({"message": f"You sticked {target_user.user.username}"})
    return Response({"message": "You cannot follow/unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_stickers(request, user_id):
    try:
        user_profile = UserProfile.objects.get(pk=user_id)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    stickers = user_profile.stickers.all()
    serializer = UserListSerializer(stickers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_sticking(request, user_id):
    try:
        user_profile = UserProfile.objects.get(pk=user_id)
    except UserProfile.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    sticking = user_profile.sticking.all()
    serializer = UserListSerializer(sticking, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_sticking(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        sticking = user_profile.sticking.all()
        serializer = UserListSerializer(sticking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({"message": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_stickers(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        stickers = user_profile.stickers.all()
        serializer = UserListSerializer(stickers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({"message": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)


# End of sticking APIs

class UserAPIView(RetrieveAPIView):
    """
    Get user details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def report_user(request):
    if request.method == 'POST':
        serializer = ReportUserSerializer(data = request.data, context={'request': request})
        
        if serializer.is_valid():
            report = serializer.save()
            response_data = serializer.data
            return Response(response_data, status= status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Report not successful'}, status= status.HTTP_400_BAD_REQUEST)
        

class ReportUserViewSet(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = ReportedUser.objects.all()
    serializer_class = ReportedUserSerializer
    lookup_field = 'user_id'


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class BusinessCategoryViewSet(viewsets.ModelViewSet):
    queryset = BusinessCategory.objects.all()
    serializer_class = BusinessCategorySerializer


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_business_profile(request):
    if request.method == 'POST':
        # Automatically associate the user's profile with the request data
        request.data['profile'] = request.user.profile.pk
        
        serializer = BusinessProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_business_profile(request, pk):
    try:
        business_profile = BusinessProfile.objects.get(pk=pk)
    except BusinessProfile.DoesNotExist:
        return Response({'detail': 'BusinessProfile not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BusinessProfileSerializer(business_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessAvailabilityListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BusinessAvailability.objects.all()
    serializer_class = BusinessAvailabilitySerializer

class BusinessAvailabilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BusinessAvailability.objects.all()
    serializer_class = BusinessAvailabilitySerializer

class BusinessProfileListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer

class BusinessProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer

class BusinessCategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BusinessCategory.objects.all()
    serializer_class = BusinessCategorySerializer

class BusinessCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BusinessCategory.objects.all()
    serializer_class = BusinessCategorySerializer

class AddressListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
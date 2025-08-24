# from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import SignupSerializer
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from rest_framework.response import Response

# User Authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'is_superuser': request.user.is_superuser,
    })
    
# Logout the user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'message': 'User logged out successfully.'}, status=200)
    

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to signup!
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                print(user)
                token, created = Token.objects.get_or_create(user=user)
                print(token.key)
                return Response({
                    'message': 'Thank you for signing up!',
                    'token': token.key,
                }, status=201)
            except IntegrityError as e:
                error_msg = str(e)
                if 'UNIQUE constraint' in error_msg and 'username' in error_msg:
                    return Response({'message': 'This username is already taken. Please choose another.'}, status=400)
                return Response({'message': 'Signup failed due to a database error.'}, status=500)
            except Exception as e:
                print("Unexpected error:", e)
                return Response({'message': 'An unexpected error occurred.'}, status=500)
        return Response(serializer.errors, status=400)
    

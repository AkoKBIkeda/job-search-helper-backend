# from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import SignupSerializer
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# User Authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'is_superuser': request.user.is_superuser,
    })
    

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
            except Exception as e:
                print(e)
                return Response({'error': 'An error occurred during signup.'}, status=500)
        return Response(serializer.errors, status=400)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    # Get all companies for the authenticated user
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Company.objects.all()
        else:
            return Company.objects.filter(user=user)

    # Create a new company for the authenticated user
    def perform_create(self, serializer):
        user = self.request.user
        print(user)
        serializer.save(user=user)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CompanyViewSet
from .views import get_current_user, SignupView, user_logout

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    path('user/', get_current_user),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', user_logout),
]
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)

from account.views import *
# define here urls http//127.0.0.1:8000//
urlpatterns = [
    path('api/register/',RegisterApiView.as_view(),name='register_api_view'),
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/',LogOutApiView.as_view(),name='logout_view'),
    
    
]

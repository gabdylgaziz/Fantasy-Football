from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/<int:id>/', getProfile),
    path('user/', UserView.as_view(), name="user_profile"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
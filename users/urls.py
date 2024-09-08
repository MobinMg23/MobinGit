from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUpAPIView, LoginAPIView, LogoutAPIView, UserPostAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('user-post/', UserPostAPIView.as_view(), name='user-post'),
]
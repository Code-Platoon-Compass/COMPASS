from django.urls import path
from .views import *

urlpatterns = [
    # path('create-user/', CreateUserView.as_view(), name='create_user'),
    # path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh/', RefreshAccessToken.as_view(), name='refresh'),
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('google-auth/', GoogleOAuthView.as_view(), name='google_oauth'),
]
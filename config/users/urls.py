from django.urls import path
from .views import loginPage, logoutUser, registerUser, userProfile, userUpdate

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
    path('profile-update/<str:pk>/', userUpdate, name='user-update'),
]
